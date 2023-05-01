+++
in_search_index = true
title="Python使用"
date=2022-11-08
updated=2023-02-28T23:18:07.000Z

[taxonomies]
categories = ["工具使用"]
tags = ["Python"]
[extra]
toc = true
comments = false
+++

# 基础

|功能|实现|
|--|--|
|float 转 int|int(num)|
|：？| (a if a > b else b)|
|将数组维度拉成一维|ravel|

**数组**

拼接数组#extend

list插入#arr.insert(0, val)

**堆**
heappush 和 heappop

> leetcode:1801

**生成随机数**

生产0~1之间的随机数

```python
import random
r = random.random()  
```

random.sample(seq, n) #随机选择一段序列，n个不一定连续

random.shuffle(seq) #打乱顺序

**全局变量的问题**

global var

记住局部变量>全局变量

**命令行**

os.system(“shell命令”)

**文件**

with open('testfile.txt','a') as file:

file.write()

## 内置函数

### zip

此函数将多个列表按照每个元素合并为一个元组。

```py
list1 = [1,2,3]
list2 = [4,5,6]

print([x for x in zip(list1,list2)])
# 输出 [(1, 4), (2, 5), (3, 6)]
# 仅仅匹配到最短的

dic1 = {1:2,3:4,5:6}

print([x for x in zip(dic1)])
# 输出 [(1,), (3,), (5,)]
```

zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。


### bisect_left

bisect()和bisect_right()等同

```py
import bisect
index = bisect.bisect_left(ls,a) #ls 是有序列表，a是目标数

#bisect_left 找有序列表中第一个大于或等于a的下标
#bisect_right 找有序列表中第一个大于a的下标

```

key 参数是3.10版本以后才添加的功能。

关键字key指定了一个方法，这个方法会接受当前数组中的中间值mid（因为二分查找就是从中间值开始的）作为其参数，然后返回一个值val，val用于跟x比较。

```py
bisect_left(range(1, 10), 5, key=lambda y: y) 
#返回： 4
```

### Counter

相当于字典

```py
c = Counter("hello world")
print(c)
# 输出：
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 相关方法
# most_common([n])：可以查找出前n个出现频率最高的元素以及它们对于的次数，也就是说频率搞的排在最前面。
# elements()：返回一个迭代器。迭代包括重复的元素。

for i in c.elements():
    print(i)
# 输出
'''
h
e
l
l
l
o
o
 
w
r
d
'''
```

用法示例：
leetcode：2363

## 修饰符

### @lru_cache(None)

在函数前加上@lru_cache(None)，表示当函数的参数相同时直接返回值不需要重复计算

# 工具集的使用

[Pandas](@blog/docs/python/python_pandas.md)

[matplotlib](@blog/docs/python/python_pyplot.md)

[Numpy](@blog/docs/python/python_numpy.md)

[Sklearn](@blog/docs/python/python_sklearn.md)

[Pytorch](@blog/docs/python/python_pytorch.md)

[Scipy](@blog/docs/python/python_scipy.md)