+++
title="Cmake使用"
date=2022-11-07
in_search_index = true

categories = ["工具使用"]
tags = ["Cmake", "编译"]

[extra]
toc = true
comments = false
+++

方便编译，再生成与各平台相关的make文件，最后执行make指令

<!--more-->

建议使用方法：

```bash
mkdir build
cd build
cmake ../   （window下：cmake -G "MinGW Makefiles" ../）
make         （window下：mingw32-make.exe）
```

参考：

> [https://blog.csdn.net/qq_39942341/article/details/106759497](https://blog.csdn.net/qq_39942341/article/details/106759497)
> 

**小点**

makefile 是由 CMakeLists.txt 生成的

## 语法

可以直接使用绝对路径，但是间隔符是 ‘/’ 而非 ‘\’

cmake的helloworld：

```cpp
#设置CMake所需的最低版本。
cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

#设置项目名，版本，语言
project(hello_test VERSION 1.0.0 LANGUAGES CXX)

#设置include文件目录
include_directories(E:/Project/Vulkan/other E:/Project/Vulkan/other2)

#执行编译命令
add_executable(hello test.cpp)
```

set

设置一个变量

FIND_LIBRARY

FIND_LIBRARY（库变量 库名 库目录）

* g++使用c17编译

-std=c++17