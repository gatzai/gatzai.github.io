+++
in_search_index = true
title="Numpy使用"
date=2022-11-08

[taxonomies]
categories = ["工具使用"]
tags = ["Python","numpy","数据处理"]
[extra]
toc = true
comments = false
+++

**插入一列**

插起来很麻烦的

### 数据结构

- np.array 转list

a.tolist()

- list 转 np.array

np.array(a)

### 矩阵

np.tile(mat, (2,2)) #重复矩阵

- 转置

arr.T  #一定要注意shape不能是（n，），而要是（n，1）

用reshape(n, 1)也行

- 特征值和特征向量

fig = np.linalg.eig(M)

- 求相关系数矩阵

np.corrcoef（matrix）#输入n行m列，输出n行n列

- concatenate

连接矩阵

x_new = np.c_[x_1,x_2]  #连接两个矩阵的列，即行数不变

- reshape

arr = arr.reshape(1, -1)  化成一行

arr = arr.reshape(-1, 1)  化成一列

- np.newaxis

增加维度

arr[：， np.newaxis] #放在后面，会给列上增加维度

arr[np.newaxis，：] #放在前面，会给行上增加维度

- squeeze

去掉一维

- np.meshgrid(x, y)

向量化为矩阵，比如x是n维，y是m维，化成m*n的矩阵，数据按照维度对齐重复填充

### 数据操作以及生成

np.sum(a,axis=0)   #列求和

np.mean #求均值

np.var #求方差

np.std #求标准差

np.divide(array1, array2, res) #逐位除

生成正态分布

np.random.randn(100)  #生成100个正态分布

线性区间

x_=np.linspace(1,10,100)  #从1到10，分割100份

生成多项式

np.ploy1d

p = np.poly1d([2,3,5,7])  #$2x^3 + 3x^2 + 5x + 7$