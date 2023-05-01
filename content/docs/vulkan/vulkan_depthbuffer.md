+++
title="Vulkan深度缓冲区"
date=2022-11-07
in_search_index = true

categories = ["工具使用"]
tags = ["Vulkan"]

[extra]
toc = true
comments = false
+++

现在我们添加第三个维度，绘制真正的3d物体。
<!--more-->

当我们画两个一上一下的正方形时，你会发现下面的正方形显示在上面，这是因为它index序号在后面，所以下面的最后才画。

有以下两种解决方案：

1. 按照深度排序所有draw calls
2. 使用深度缓冲的深度测试

第一个方案一般用于透明物体的绘制，对于不透明物体的排序第二个方案才是常用的。

A depth buffer is an additional attachment that stores the depth for every position, just like the color attachment stores the color of every position.

深度缓冲的格式有带模板测试的和不带模板测试的。

跳过：**Explicitly transitioning the depth image**

因为我们会在renderpass做

三部搞定深度测试

1. 创建：depth image
2. RenderPass添加：深度附件
3. Framebuffer添加：depthImageView

评论区第一个问题不错。是关于：为什么由于信号量的控制，同一时间只能运行一个subpass？