+++
title="Transformer学习笔记"
date=2023-01-24
lastmod=2023-01-24
in_search_index = true
categories = ["学习笔记"]
tags = ["深度学习"]

[extra]
toc = true
comments = true
+++

<center>
    <img style="width: 100%; height: 300px; object-fit: cover;object-position:50% 50%;" value='transformer' src='https://img.picgo.net/2023/01/24/IMG_20221219_114753_57086b12b4e9148e905.jpeg'/>
</center>

<!-- more -->

## 注意力机制

在注意力机制中，通过随意线索query，来选择环境中的不随意线索key以及匹配的value。

比方说，我突然想喝咖啡了（query），我前面有几种咖啡，火腿等其他零食（key），我就会特别注意咖啡，而且我比较喜欢喝酸味较低的咖啡（value）。

60年代的非参注意力机制：nadaraya核方法

注意力的通用公式：f(x) = a(x,xi)hi

注意力分数：q和k的相似度

注意力权重：softmax的结果

两种常见的注意力分数计算：

- 加
    
    当q，k，v结构不一样时
    
    Wk（h*k），Wq（h*v），这里h是超参数
    
    a（q，k） = V*tanh(Wk*K + Wq*Q)
    
    等价于将K和q合并起来后放入到一个隐藏成大小为H输出唯一的单层L P中。
    
- 点乘

注意力机制+rnn

### 多头注意力

学习不同的特征

每个头都有独自的Q K V。

## Transformer架构

与seq2seq不同，transformer没有rnn而是基于纯注意力机制。

### 层归一化

比较稳定
