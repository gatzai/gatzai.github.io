+++
in_search_index = true
title="Vulkan贴图"
date=2022-11-07

categories = ["工具使用"]
tags = ["Vulkan"]

[extra]
toc = true
comments = false
+++

Vulkan贴图
<!--more-->

### 步骤大纲

1. 创建image对象，该对象backed by device memory
2. 像素填充，从image file
3. 创建image采样
4. iamge采样描述符 从纹理中采样颜色

我们之前以及在swapchain里面使用锅了image对象，但是那是由swapchain自动创建的。

现在我们就要自己创建image对象，这个过程和创建vertex缓冲区很相似。

image有不同的layout，决定着像素如何在内存中排列，比如：

VK_IMAGE_LAYOUT_PRESENT_SRC_KHR ：显示到屏幕用

VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL ：从片段着色器写入颜色用

VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL ：源转移用

VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL ：目标转移用

VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL ： 从着色器采样用

最常用的方法是pipeline barrier，它易于处理资源同步读取。也可以用于转换图像布局，转移队列族拥有组。

图像对象内的像素称为纹素。

执行布局转换的最常见方法之一是使用图像内存屏障。

评论区有个问题是每帧都要更新图片，该如何处理。

这里我还想到了，同一张图片多次使用的情况，修改图片的情况。

### imageview和采样

shader可以直接从image中读取纹素，但作为贴图时并不会这样用。贴图通常会经过采样，然后再给shader。

欠采样(Undersampling)问题：纹素数据大于fragment，比如锐角视角看一个棋盘，远方的片段就很小，但是纹素数据还是不变，这会导致artifacts。这个问题可以通过sampler的各向异性过滤解决。

### 绑定image 采样

这一节我们使用一个新的描述符：c*ombined image sampler*

这个描述符可以让shader通过采样对象读取图片信息

首先给 descriptor 的 layoutInfo 再添加一个 binding。然后pool，最后descriptor set。接着修改shader