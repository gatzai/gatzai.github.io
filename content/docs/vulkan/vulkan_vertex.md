+++
in_search_index = true
title="Vulkan顶点缓冲区"
date=2022-11-07

categories = ["工具使用"]
tags = ["vulkan"]
[extra]
toc = true
comments = false
+++

使用in关键字从缓冲区获取数据

<!--more-->

（去掉了gl_VertexIndex，这个应该是顶点序号）

在shader上传到GPU前，我们需要把数据传到shader中。我们需要设置两种结构

1. VkVertexInputBindingDescription： 用于构造合适的数据
2. VkVertexInputAttributeDescription ：指明如何提取数据

通过vertexInputInfo，将顶点数据传输到渲染管线中。

### 创建顶点缓冲区

Vulkan中的缓冲区存取的数据可以被显卡读取，可以用于传送坐标或其他数据，但是它并不会自动分配内存空间，所以要手动创建。

1. 创建缓冲区
2. 获取存储空间
3. 分配
4. 填充数据
5. 提交数据

### 更加高效地复制数据

最高效地内存有`VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT`的标记，并且其一般不能被CPU直接访问

所以我们需要创建两个vertex buffer，一个在CPU上由CPU读取并存放数据，另外一个在GPU上。

创建一个独立的command pool，因为这是一个短周期的

`[vkAllocateMemory]` 资源有限，不应该为每个独立的缓冲区都建立，而是要统一管理。通过VkPhysicalDeviceLimits::maxMemoryAllocationCount来查看。

### 顶点序号

这个序号也需要创建一个buffer，和之前的顶点buffer一样，不同的是，这里使用了VK_BUFFER_USAGE_INDEX_BUFFER_BIT。

然后就是使用indexbuffer了：

1. 绑定，vkCmdBindIndexBuffer
2. 替换 vkCmdDraw 为 vkCmdDrawIndexed

完成

拓展：

当然这两个buffer也用一个buffer来代替，使用offset来确定不同的数据。这样临近的结构无疑对缓存更加友好。如果在相同的渲染操作期间没有使用它们，甚至可以为多个资源重用相同的内存块，当然前提是它们的数据被刷新。

**文章摘录：Vulkan内存管理**

> [https://developer.nvidia.com/vulkan-memory-management](https://developer.nvidia.com/vulkan-memory-management)
> 

**前言**

OpenGL会帮我们做大部分内存管理的工作，所以开发起来方便快捷。

但是Vulkan里面，我们需要自己去实现，而且要具体问题具体分析。

这里有几个情形，帮助我们更好地利用内存：

1. 分配内存通常涉及到昂贵的系统操作
2. 重用比分配更高效
3. 连续的数据对缓存友好
4. 对齐的数据能让硬件处理更快

**内存结构**

Heap：硬件相关的存储结构

Memory type：你需要选择正确的类型来适应相应的资源

等
使用in关键字从缓冲区获取数据

（去掉了gl_VertexIndex，这个应该是顶点序号）

在shader上传到GPU前，我们需要把数据传到shader中。我们需要设置两种结构

1. VkVertexInputBindingDescription： 用于构造合适的数据
2. VkVertexInputAttributeDescription ：指明如何提取数据

通过vertexInputInfo，将顶点数据传输到渲染管线中。

### 创建顶点缓冲区

Vulkan中的缓冲区存取的数据可以被显卡读取，可以用于传送坐标或其他数据，但是它并不会自动分配内存空间，所以要手动创建。

1. 创建缓冲区
2. 获取存储空间
3. 分配
4. 填充数据
5. 提交数据

### 更加高效地复制数据

最高效地内存有`VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT`的标记，并且其一般不能被CPU直接访问

所以我们需要创建两个vertex buffer，一个在CPU上由CPU读取并存放数据，另外一个在GPU上。

创建一个独立的command pool，因为这是一个短周期的

`[vkAllocateMemory]` 资源有限，不应该为每个独立的缓冲区都建立，而是要统一管理。通过VkPhysicalDeviceLimits::maxMemoryAllocationCount来查看。

### 顶点序号

这个序号也需要创建一个buffer，和之前的顶点buffer一样，不同的是，这里使用了VK_BUFFER_USAGE_INDEX_BUFFER_BIT。

然后就是使用indexbuffer了：

1. 绑定，vkCmdBindIndexBuffer
2. 替换 vkCmdDraw 为 vkCmdDrawIndexed

完成

拓展：

当然这两个buffer也用一个buffer来代替，使用offset来确定不同的数据。这样临近的结构无疑对缓存更加友好。如果在相同的渲染操作期间没有使用它们，甚至可以为多个资源重用相同的内存块，当然前提是它们的数据被刷新。

**文章摘录：Vulkan内存管理**

> [https://developer.nvidia.com/vulkan-memory-management](https://developer.nvidia.com/vulkan-memory-management)
> 

**前言**

OpenGL会帮我们做大部分内存管理的工作，所以开发起来方便快捷。

但是Vulkan里面，我们需要自己去实现，而且要具体问题具体分析。

这里有几个情形，帮助我们更好地利用内存：

1. 分配内存通常涉及到昂贵的系统操作
2. 重用比分配更高效
3. 连续的数据对缓存友好
4. 对齐的数据能让硬件处理更快

**内存结构**

Heap：硬件相关的存储结构

Memory type：你需要选择正确的类型来适应相应的资源

等