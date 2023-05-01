+++
title="CPP_STL笔记"
date=2022-11-07
lastmod=2022-11-18
in_search_index = true

categories = ["工具使用"]
tags = ["Cpp","编程","STL"]

[extra]
toc = true
comments = false
+++

array和数组的区别：

array支持容器操作

**vector**

排序的使用：

```cpp
sort(arr.begin(), arr.end(),[](const twonum& pre, const twonum& next){
            return pre.b < next.b;  //升序
        });
//中括号里面加&表示外部引用，即函数体内引用外部变量
```

data()：返回内置vecotr所指的数组内存的第一个元素的指针

初始化：vector<int> arr(a, b)，初始化a个b元素

二维vector初始化：vector<vector<int>> tag(n, vector<int>(n));

swap（arr[i]，arr[j]）

lower_bound() 

用于在指定区域内查找不小于目标值的第一个元素

如果是递减则，lower_bound(arr.begin(), arr.end(), val, greater<int>); //找第一个小于或等于val的数。

nth_element

数组中第n小的数

reduce（和accumulate相似）

累加数组中的元素

unique()

去除相邻的重复元素，其实就是把重复的数放到最后，返回不重复的尾地址。

**priority_queue**

1. priority_queue<int> q;
2. priority_queue<int, vector<int>, less<int> > q;   （用来承载数据结构的）

新东西：

**emplace_back**

直接在容器尾部创建对象，省去了拷贝和移动的操作

std::optional

以安全的方式返回对象

accumulate  #偷懒的累加，不好用

accumulate(v.begin(),v.end(),0LL)  //第三个参数为初始值

**更多请参考**
> https://learn.microsoft.com/zh-cn/cpp/standard-library/algorithm?view=msvc-170