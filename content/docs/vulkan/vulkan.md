+++
title="Vulkan笔记"
date=2022-11-07
in_search_index = true

categories = ["工具使用"]
tags = ["vulkan"]

[extra]
toc = true
comments = false
+++

我用openGL画过三角形啦，游戏引擎也把玩过unity3d和godot了，shader也玩过一段时间了。

vulkan是未来，现在可以开始学习了。
<!--more-->

## 准备工作

### 学习资源

视频：[https://www.bilibili.com/video/BV1Vu411R7cb?vd_source=be64fb00ff66079e029634bb4dd1f1bf](https://www.bilibili.com/video/BV1Vu411R7cb?vd_source=be64fb00ff66079e029634bb4dd1f1bf)

文档：[https://vulkan-tutorial.com/](https://vulkan-tutorial.com/)

[https://zhuanlan.zhihu.com/p/339592354](https://zhuanlan.zhihu.com/p/339592354)

### 环境搭建

[https://blog.csdn.net/weixin_43475995/article/details/121516284](https://blog.csdn.net/weixin_43475995/article/details/121516284)

### 目标

渲染一个场景：有水，树林，山，一天循环

还可以结合陈文礼大佬的引擎工程，去了解如何整合其他工具

### 辅助知识点

GPU 端 显存，这块存储位于芯片内部，叫Local Memory. 

CPU 端 系统内存，这块存储即平常所说内存，叫host Memory。

### 一些单词

artifacts 瑕疵（百度，我觉得这个翻译比较适合），伪影（谷歌），假象（百度搜索）

### 资源管理

使用C++实现自动资源管理

RAII is the recommended model for larger Vulkan programs

there is one parameter that they all share: `pAllocator`This is an optional parameter that allows you to specify callbacks for a custom memory allocator

## 画一个三角形

### 创建vulkan实例

…

### 验证层

The Vulkan API is designed around the idea of minimal driver overhead。所以很少有检错机制，你要真正知道你在做什么，不然程序很容易崩溃。

但这并不意味着无法检错，验证层可能是个好帮手。

验证层的通常用法：

1. 检测错误使用的参数
2. 资源泄露
3. 线程安全
4. 输出日志
5. 分析调用

有两种验证层：实例 和 特定设备

有点懵

### Debug

先验证是否能用validation layer

`pNext`
even the debug callback in Vulkan is managed with a handle that needs to be explicitly created and destroyed. 

需要创建和销毁，

1. 创建就需要一些信息初始化，通过Info结构来初始化。
2. 初始化信息需要给一个特定的函数，因为是拓展，这个函数不会自动加载，所以需要找到其地址，然后用代理函数加载。
3. 最后是销毁函数。

### 选择物理设备

获取方式和获取拓展一样的

还需要检测显卡是否可用

### **Queue families**

In Vulkan, anything from drawing to uploading textures, requires commands to be submitted to a queue.

### 逻辑设备

An example of a device specific extension is `VK_KHR_swapchain`

### 对Window系统

由于vulkan是平台无关的，所以需要做一些win相关的工作，使用WSI拓展

我想，窗口只是画框，而这个suface就是画布

创建，初始化，销毁

查询支持的设备

### **Swap chain 交换链**

就是一个图像队列

1. 检查是否支持
2. 启用设备拓展
    
    Using a swapchain requires enabling the `VK_KHR_swapchain` extension first
    
3. 需要初始化更多的细节
    1. Basic surface capabilities 
    2. Surface formats 格式
    3. Available presentation modes 模式
4. 正确的设置
    - Surface format (color depth)
    - Presentation mode (conditions for "swapping" images to the screen) 最重要的
    - Swap extent (resolution of images in swap chain)
5. 创建swap chain
    
    初始化结构体
    

一些功能：

* 设置图像的数量
* 获取图像
* 图像格式
* 颜色空间
* 分辨率extent
* 可用于后处理等功能imageUsage

### 图像的显示

每个swapchainimage 都有一个 imageview

To use any `[VkImage]`, including those in the swap chain, in the render pipeline we have to create a `[VkImageView]`object

创建和销毁

这个甚至还提到了VR那种双显示屏的方式，所以要遍历swapchain

An image view is sufficient to start using an image as a texture, but it's not quite ready to be used as a render target just yet。 image view可以用于贴图，但并不能用于渲染目标。

确定是1维2维3维还是cubemap：viewType

图像用于什么目的，单纯颜色，还是mipmap

### 着色器

shader code in Vulkan has to be specified in a bytecode. This bytecode format is called [SPIR-V](https://www.khronos.org/spir)

1. 我们使用glsl来写shader，然后编译。
    
    VulkanSDK里面有编译工具，但是我们也可以直接从代码里面编译。The Vulkan SDK includes [libshaderc](https://github.com/google/shaderc), which is a library to compile GLSL code to SPIR-V from within your program.
    
2. 加载编译完的shader
    
    直接加载二进制文件即可
    
3. Before we can pass the code to the pipeline, we have to wrap it in a `[VkShaderModule]`object.
4. 最后需要把着色器注册到相应的管线（VkPipeline）上

### 固有功能

1. 动态状态
    
    If you want to use dynamic state and keep these properties out, then you'll have to fill in a VkPipelineDynamicStateCreateInfo structure like this:
    
    This will cause the configuration of these values to be ignored and you will be able (and required) to specify the data at drawing time.
    
2. 顶点输入
    
    将顶点传输到vertexshader
    
3. 输入装配
    
    几何体的绘制方式
    
4. 视图和裁剪
    
    it's is possible to use multiple viewports and scissor rectangles on some graphics cards,
    
5. 光栅化
    
    It also performs depth testing, face culling and the scissor test, and it can be configured to output fragments that fill entire polygons or just the edges (wireframe rendering). All this is configured using the VkPipelineRasterizationStateCreateInfo structure.
    
6. 多重采样
    
    抗锯齿
    
7. 深度图和模板测试
    
    If you are using a depth and/or stencil buffer, then you also need to configure the depth and stencil tests using `[VkPipelineDepthStencilStateCreateInfo]`
    
8. 颜色混合
9. 管线框架
    
    使用shader的uniform 
    
    the uniform and push values referenced by the shader that can be updated at draw time
    

### Render passes

we need to tell Vulkan about the framebuffer attachments that will be used while rendering.

renderpass用于确定有多少个颜色和深度缓冲区，每个缓冲区使用多少个样本，以及在渲染操作中如何处理其内容

renderpass的作用：多重采样，颜色、深度、模板图像的清除和保留，图像的操作方式（后面再讲）

一个renderpass还有多个subpass

多个subpass的例子就是后处理，游戏画面需要多种后处理方式，多个subpass与多个renderpass相比会有更好的性能。

Subpasses是后续渲染操作，取决于先前通道中帧缓冲(framebuffer)区的内容。

### 阶段性总结：

图形管线的设置包括但不仅限于：

1. 着色器：pStages
2. 顶点输入：pVertexInputState
3. 顶点装配：pInputAssemblyState
4. 视图状态：pViewportState
5. 光栅化信息：pRasterizationState
6. 多采样：pMultisampleState
7. 颜色混合：pColorBlendState
8. 动态状态：pDynamicState
9. 布局：layout
10. 渲染通道：renderPass
11. 。。。

### Frame Buffer

每个framebuffer都要对应swapChainImageViews，因为从swapchain获取imageview时需要放到对应的framebuffer中。

每个framebuffer需要指定renderpass，pAttachments用于确定imageview等

### Command buffer

这是绘制命令，并不直接调用，而是一起提交，这样更高效。除此之外，还用于多线程。

有三种执行方式，暂时还没用到

### 画出你的三角形

渲染循环：

1. 等待前一帧渲染完毕（CPU）
2. 从swapchain中获取图像（CPU）
3. 记录commandbuffer，（CPU）
4. 提交commandbuffer（CPU→GPU）
5. 展示swapchain的图片（GPU→CPU）

同步

使用semaphore和fence

* fence用于CPU（host）的同步

* semaphore用于队列和队列间的同步

三个同步变量：

inFlightFence：用于等待上一帧完毕，一帧渲染一次

imageAvailableSemaphore：用于等待swapchain的图像能够用于渲染

renderFinishedSemaphore：用于等待渲染完毕，是否可以展示

因为有三个操作是同步执行的：vkAcquireNextImageKHR，vkQueueSubmit，vkQueuePresentKHR。

整个流程下来，一些关键的概念还缺乏一些流程图。不过可以在网上找。

现在对整个流程都清晰了。

### 多帧同时渲染

我们可以让CPU多干点活

每一帧都需要一个commandbuffer，同步标记等。

哪里有多线程？这里是并发，可能是多个commandBuffers产生的并发。

所以这里默认是上一帧渲染完是比我们程序执行一次迭代要慢的。

### 修改swapchain，以适应窗口尺寸的变化

需要等待渲染完毕才重建swapchain，要避免一直等待，如果提前reset了信号，那么就会永远卡在fence的等待了，因为重建swapchain立刻返回了，没有任何操作能够给fence信号。

我电脑可以正确处理VK_ERROR_OUT_OF_DATE_KHR的问题，所以这部分我就不写了。

评论区有另一个方法，应该是一个tradeoff