

<h1 align="center"> FaceNet人脸检测追踪系统</h1>
<p align="center">
  <a href="README.md"><strong>English</strong></a> | <strong>简体中文</strong>
</p>



## 目录

- [仓库简介](#项目介绍)
- [前置条件](#前置条件)
- [镜像说明](#镜像说明)
- [获取帮助](#获取帮助)
- [如何贡献](#如何贡献)

## 项目介绍

[FaceNet](https://github.com/timesler/facenet-pytorch) 是一种人脸识别系统，使用facenet-pytorch和streamlit构建人脸检测应用，支持用户上传视频自动检测出人脸位置进行追踪。本商品基于鲲鹏服务器的Huawei Cloud EulerOS 2.0 64bit系统，提供开箱即用的FaceNet。

## 核心特性

- **高精度实时人脸检测：** 基于 MTCNN（Multi-task Cascaded Convolutional Networks）模型，支持在复杂场景下准确检测多张人脸，具备良好的鲁棒性和定位精度
- **轻量高效，适合边缘部署：** MTCNN 模型体积小、推理速度快，适合在资源受限设备上部署，兼顾性能与效率

本项目提供的开源镜像商品 [FaceNet人脸检测追踪系统](https://marketplace.huaweicloud.com/hidden/contents/5d1783b2-07da-4000-83fd-69d3a1f5187c#productid=OFFI1138678404113182720) 已预先安装2.5.3版本的FaceNet及其相关运行环境，并提供部署模板。快来参照使用指南，轻松开启“开箱即用”的高效体验吧。

> **系统要求如下：**
>
> - CPU: 2vCPUs 或更高
> - RAM: 4GB 或更大
> - Disk: 至少 40GB

## 前置条件

[注册华为账号并开通华为云](https://support.huaweicloud.com/usermanual-account/account_id_001.html)

## 镜像说明

| 镜像规格                                                     | 特性说明                                                 | 备注 |
| ------------------------------------------------------------ | -------------------------------------------------------- | ---- |
| [FaceNet-2.5.3-kunpeng](https://github.com/HuaweiCloudDeveloper/facenet-image/tree/FaceNet-2.5.3-kunpeng) | 基于鲲鹏服务器 + Huawei Cloud EulerOS 2.0 64bit 安装部署 |      |

## 获取帮助

- 更多问题可通过 [issue](https://github.com/HuaweiCloudDeveloper/facenet-image/issues) 或 华为云云商店指定商品的服务支持 与我们取得联系
- 其他开源镜像可看 [open-source-image-repos](https://github.com/HuaweiCloudDeveloper/open-source-image-repos)

## 如何贡献

- Fork 此存储库并提交合并请求
- 基于您的开源镜像信息同步更新 README.md
