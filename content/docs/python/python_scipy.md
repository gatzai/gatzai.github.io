+++
in_search_index = true
title="Scipy使用"
date=2022-11-08

[taxonomies]
categories = ["工具使用"]
tags = ["Python","scipy"]
[extra]
toc = true
comments = false
+++

### 最小二乘法

leastsq(func, x0, args=()) 

func:误差函数  （真实值减去估计值）

x0: 起始估计的参数值  （随便写，维度对就行。参数越多拟合程度越高，因为是多项式拟合）

args: 拟合的数据样本 

> 参考：[https://www.jb51.net/article/240964.htm](https://www.jb51.net/article/240964.htm)

### 线性规划

使用res=optimize.linprog(c,A,b,Aeq,beq,bounds)

注意：系统默认是小于等于且求最小值，所以一切大于等于的不等式都要在两边同时乘以-1

例子：

求$max z = 2*x_1 + 3*x_2 - 5*x_3$

s.t. 有：

$x_1 + x_2 + x_3 = 7$

$2*x_1 -5*x_2 + x_3 ≥ 10$

$x_1 + 3*x_2 + x_3 ≤ 12$

$x_1, x_2, x_3 ≥ 0$

```python
from scipy import optimize
import numpy as np
c = np.array([2,3,-5])
A = np.array([[-2,5,-1],[1,3,1]])
b = np.array([-10,12])
Aeq = np.array([[1,1,1]])
beq = np.array([7])
x1 = (0,None)
x2 = (0,None)
x3 = (0,None)
res=optimize.linprog(-c,A,b,Aeq,beq,bounds=(x1,x2,x3)  #默认最小，所以最大就加个负号
```

结果存在x：array

> 参考：[https://blog.csdn.net/m0_59309242/article/details/119352731](https://blog.csdn.net/m0_59309242/article/details/119352731)
