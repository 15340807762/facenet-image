import streamlit as st
import tempfile
import cv2
import torch
from PIL import Image
from facenet_pytorch import MTCNN
import os
import subprocess
import base64

st.title("🎥 视频人脸检测并播放")

uploaded_file = st.file_uploader("📤 上传MP4视频", type=["mp4"])

if uploaded_file is not None:
    # 保存上传的视频文件
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tfile:
        tfile.write(uploaded_file.read())
        input_video_path = tfile.name

    st.info(f"✅ 上传成功，路径: `{input_video_path}`")

    # 初始化 MTCNN
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    mtcnn = MTCNN(keep_all=True, device=device)

    # 打开视频
    cap = cv2.VideoCapture(input_video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 创建临时目录保存帧
    temp_dir = tempfile.TemporaryDirectory()
    frame_output_dir = temp_dir.name

    progress_bar = st.progress(0)
    frame_idx = 0

    # 遍历帧并处理
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        boxes, _ = mtcnn.detect(img)

        if boxes is not None:
            for box in boxes:
                x1, y1, x2, y2 = [int(b) for b in box]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # 保存处理后的帧为图片
        frame_path = os.path.join(frame_output_dir, f"frame_{frame_idx:06d}.png")
        cv2.imwrite(frame_path, frame)

        frame_idx += 1
        progress_bar.progress(min(frame_idx / total_frames, 1.0))

    cap.release()
    progress_bar.empty()

    st.text("🎬 正在合成新的视频（使用 FFmpeg）...")

    output_video_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4").name

    # 使用 FFmpeg 合成视频
    cmd = [
        "ffmpeg",
        "-y",
        "-framerate", str(int(fps)),
        "-i", os.path.join(frame_output_dir, "frame_%06d.png"),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-profile:v", "baseline",
        "-level", "3.0",
        "-movflags", "+faststart",
        "-vf", f"scale={width}:{height}",
        output_video_path
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        st.error("❌ FFmpeg 生成视频失败！")
        st.text(result.stderr.decode())
    else:
        st.success("✅ 视频生成成功，开始播放！")

        # 以 base64 编码确保网页能播放
        def get_video_base64(path):
            with open(path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()

        video_b64 = get_video_base64(output_video_path)
        video_html = f"""
        <video width="100%" height="auto" controls>
            <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
            您的浏览器不支持播放该视频。
        </video>
        """
        st.markdown(video_html, unsafe_allow_html=True)

    # 清理临时资源
    temp_dir.cleanup()
    try:
        os.unlink(input_video_path)
        os.unlink(output_video_path)
    except Exception as e:
        st.warning(f"⚠️ 清理临时文件时出错: {e}")
else:
    st.info("请上传一个MP4格式的视频文件进行处理 🎞️")
