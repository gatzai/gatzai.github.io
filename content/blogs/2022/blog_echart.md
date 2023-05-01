+++
title="echart之地图数据可视化"
date=2022-11-29
updated=2022-11-29
in_search_index = true

categories = ["可视化"]
tags = ["echart","可视化"]

[extra]
toc = true
comments = true 
+++

许久没用过 echart 了，感觉做数据处理可视化还是很重要的。以前总是用了就丢掉，现在有了博客就方便多了。

<!-- more -->

## 简介

这个小项目主要是可视化一些中国企业在不同年份的迁移过程。

## 实现过程

### 包含文件

* geoinfo.json,  中国县及以上行政区的经纬度
* changjiang.json, 长江的多边形点
* allpos_t.json, 数据集

### 过程
经过了一段痛苦的编码解码过程，终于把数据打包成了json，主要包括：企业编码，年份，地址（省，市，县区，乡镇，街道）

主要实现就是通过‘县区’和‘乡镇’这两个索引来获取经纬度。然后绘制出来。

### 亮点

这里面有一个判断点是否在多边形内部的算法，我验证过是可以用的，但是还没有去理解。

## 现存问题

echart散点图多点重合问题

## 成果

[企业迁移图](https://github.com/silentbluedrop/EchartVisual.git)