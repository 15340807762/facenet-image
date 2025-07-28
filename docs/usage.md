# FaceNet人脸检测追踪系统使用指南



# 一、商品链接



[FaceNet人脸检测追踪系统](https://marketplace.huaweicloud.com/hidden/contents/5d1783b2-07da-4000-83fd-69d3a1f5187c#productid=OFFI1138678404113182720)

# 二、商品说明



FaceNet是一种人脸识别系统，使用facenet-pytorch和streamlit构建人脸检测应用，支持用户上传视频自动检测出人脸位置进行追踪。系统通过MTCNN算法对每一帧视频图像进行识别分析，实时标注人脸位置。本商品通过鲲鹏服务器+EulerOS2.0进行安装部署

# 三、商品购买



您可以在云商店搜索 **FaceNet人脸检测追踪系统**。

其中，地域、规格、推荐配置使用默认，购买方式根据您的需求选择按需/按月/按年，短期使用推荐按需，长期使用推荐按月/按年，确认配置后点击“立即购买”。

## 3.1 使用 RFS 模板直接部署



![img.png](images/img1.png) 
必填项填写后，点击 下一步
![img.png](images/img2.png)
![img.png](images/img3.png)
创建直接计划后，点击 确定
![img.png](images/img4.png)
![img.png](images/img5.png)
点击部署，执行计划
![img.png](images/img6.png)
如下图“Apply required resource success. ”即为资源创建完成
![img.png](images/img7.png)

# 3.2ECS 控制台配置



### 准备工作



在使用ECS控制台配置前，需要您提前配置好 **安全组规则**。

> **安全组规则的配置如下：**
>
> - 入方向规则放通端口8501，必须包含这些端口才能正常访问使用
> - 入方向规则放通 CloudShell 连接实例使用的端口 `22`，以便在控制台登录调试
> - 出方向规则一键放通

### 创建ECS



前提工作准备好后，选择 ECS 控制台配置跳转到[购买ECS](https://support.huaweicloud.com/qs-ecs/ecs_01_0103.html) 页面，ECS 资源的配置如下图所示：

选择CPU架构 
![img.png](images/img8.png)
选择服务器规格 ![img.png](images/img9.png)
选择镜像 ![img.png](images/img10.png)
其他参数根据实际请客进行填写，填写完成之后，点击立即购买即可 
![img.png](images/img11.png)

> **值得注意的是：**
>
> - VPC 您可以自行创建
> - 安全组选择 [**准备工作**](#准备工作) 中配置的安全组；
> - 弹性公网IP选择现在购买，推荐选择“按流量计费”，带宽大小可设置为5Mbit/s；
> - 高级配置需要在高级选项支持注入自定义数据，所以登录凭证不能选择“密码”，选择创建后设置；
> - 其余默认或按规则填写即可。

# 商品使用



## FaceNet使用

conda activate facenet

cd /home/facenet-pytorch/examples

streamlit run app.py

然后使用ip+8501来打开网页进行检测识别

![img.png](images/img_1.png)

上传人脸视频进行检测追踪。

![img.png](images/img_2.png)

### 参考文档



[FaceNet官方文档](https://github.com/timesler/facenet-pytorch)

