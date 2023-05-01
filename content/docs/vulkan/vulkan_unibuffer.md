+++
in_search_index = true
title="Vulkan统一缓冲区"
date=2022-11-07

categories = ["工具使用"]
tags = ["vulkan"]

[extra]
toc = true
comments = false
+++

Uniform buffer

也就是公共区域，给所有shader的全局变量

比如模型，视图，投影矩阵。

<!--more-->

### 使用描述符

描述符是着色器自由访问缓冲区和图像等资源的一种方式。

有很多种描述符，在这节，我们将使用uniform buffer objects相关的。

使用描述符有三个步骤：

1. 在pipeline创建时指定一个描述符
2. 从描述符池中分配描述符集
3. 绑定描述符

### 创建descriptor layout

创建unifrom缓冲区

输入变换数据

Using a UBO this way is not the most efficient way to pass frequently changing values to the shader. A more efficient way to pass a small buffer of data to shaders are *push constants*
. We may look at these in a future chapter.

当前用的这种方式来更新变换矩阵并不算高效。

### shader访问数据

接下来，shader需要访问相关数据了

通过描述符池来创建描述符集，使用描述符集来获取缓冲区的数据。

创建描述符池

创建描述符集：给每个描述符集添加uniformBuffers，通过vkUpdateDescriptorSets来更新配置

使用描述符集

由于y轴反转了，所以我们要换成逆时针绘制才能看到结果

记得每个缓冲帧都需要创建描述符集

与顶点和索引缓冲区不同，描述符集不是图形管道独有的。 因此，我们需要指定是否要将描述符集绑定到图形或计算管道。

在创建管线的时候，为什么可以在pipelineLayoutInfo指定多个描述符集布局，因为一个已经包含所有绑定。

### 额外话题：对齐

不对齐的话，是会出问题的

### 以上两种方式传数据给shader有什么区别，各有什么特点？

传送顶点和序号：vkCmdBindVertexBuffers，vkCmdBindIndexBuffer

传送uniform：vkCmdBindDescriptorSets