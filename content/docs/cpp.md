+++
title="CPP笔记"
date=2022-11-07
in_search_index = true

categories = ["工具使用"]
tags = ["Cpp","编程"]

[extra]
toc = true
comments = false
+++

### lambda函数

```cpp
auto toNumber = [&](string const& s) -> unsigned {
...
}
```
|形式|解释|
|--|--|
[]|定义匿名函数
[&]|以引用形式捕获所有外部变量，也就是外部变量均可用
(string const &s) |匿名函数的参数
->|定义匿名函数
unsigned|函数返回值类型
{...}|函数实现体

### uint32_t， size_t，int

size_t：适用于移植，表示对应平台的无符号整型

uint32_t：则显示地考虑到是否会溢出

### string

string 没有replace

string → int : atoi

max_element（arr+first,arr+last）//返回数组最大值的位置

*max_element（arr+first,arr+last）//返回数组最大值

### **lower_bound 与 upper_bound**

用法：

数组必须有序，当有多个相同时，lower就是第一个大于等于n的，upper就是第一个大于n的

[https://codeforces.com/blog/entry/107962](https://codeforces.com/blog/entry/107962) 的C题

找bound的序号：减去开始的迭代器

若找不到，则返回end迭代器。

### next_permutation

产生全排列

next_permutation(nums.begin(), nums.end());

### tuple

get<0>(tuple)  获取tuple的第0个数据

### **mt19937（C++11）**

属于库 <random>

初始随机化引擎：mt19937 gen{random_device{}()};  //高效的随机化，范围大，周期长

随机数分布类：uniform_real_distribution<double> dis;  //根据种子生成特定范围的随机数，均匀分布，输入必须是随机化引擎。
* uniform_int_distribution<int> //均匀分布(整形)
* normal_distribution<> dis(a,b)//正态分布

获取随机数：dis(gen)

```cpp
#include <random>

mt19937 gen{random_device{}()};
uniform_int_distribution<int> dis(1,5); //整型分布，两边取闭区间
cout << dis(gen) << endl;
```

### **optional（C++17）**

表示暂时没有

`std::optional<T>`类型的变量要么是一个`T`类型的**变量**，要么是一个表示“什么都没有”的**状态**

比如一个string，我是不能给它NULL，所以无法给它一个暂未赋值的状态，这里空字符串也是一个赋值状态。

而又了optional，我们可以用 has_value() 去查询。用 value() 来获取值。

参考：

[https://zhuanlan.zhihu.com/p/251306766?utm_source=wechat_session](https://zhuanlan.zhihu.com/p/251306766?utm_source=wechat_session)

### **move**

以非常简单的方式将左值引用转换为右值引用

move操作实际上是系统将这一块地址属于哪一个地址的登记改一下，实际上这一块内存根本没有发生任何变化

用法：比如一个vector赋值给另外一个vector：v2=move(v1);

左值：指表达式结束后依然存在的持久对象，可以取址，

右值：指表达式结束后不再存在的临时对象，不可以取址，

### **Semaphore 信号量**

sem_t ：变量

sem_init ：初始化

sem_wait ： P操作，减1

sem_post ： V操作，加1

### **Fence 内存屏障**

现代编译器的代码优化和编译器指令重排可能会影响到代码的执行顺序，两行逻辑无关的代码可能会重排，但这会导致一些糟糕的后果。

使用内存屏障，就是我们使用具有同步语义的指令来标记真正需要同步的变量和操作，告诉CPU和编译器不要对这些标记好的同步操作和变量做违反顺序一致性的优化，而其它未被标记的地方可以做原有的优化，这样就可以解决指令重排导致的问题。

主要有：

1. 编译器在生成指令时做了重排
2. CPU在执行时做了指令重排

参考：[https://blog.csdn.net/zhuhongshu/article/details/111327141](https://blog.csdn.net/zhuhongshu/article/details/111327141)

alignas对齐

参考：[https://blog.csdn.net/m0_68070522/article/details/124537265?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2~default~CTRLIST~Rate-1-124537265-blog-119536133.pc_relevant_multi_platform_featuressortv2dupreplace&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2~default~CTRLIST~Rate-1-124537265-blog-119536133.pc_relevant_multi_platform_featuressortv2dupreplace&utm_relevant_index=1](https://blog.csdn.net/m0_68070522/article/details/124537265?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-124537265-blog-119536133.pc_relevant_multi_platform_featuressortv2dupreplace&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-124537265-blog-119536133.pc_relevant_multi_platform_featuressortv2dupreplace&utm_relevant_index=1)


**内建函数**

__builtin_popcount

用于计算一个 32 位无符号整数有多少个位为1


### 结构体
**声明**

1. struct Mystruct{};
    
    定义：struct Mystruct ms;  //C写法
    
    Mystruct ms;  //C++写法
    
    不推荐。
    
2. struct Mystruct{} * mst;
    
    说明：相当于定义了一个Mystruct，同时定义了一个指针变量。不推荐这样用
    
3. struct {} mystruct;
    
    只是定义了一个mystruct变量，一次性使用的。不推荐这样写
    
4. typedef struct {} Mystruct;
    
    定义：Mystruct ms;  //C, C++均可
    
5. typedef struct Mystruct {} Mst;
    
    定义：如果使用C，则可以使用Mst；如果使用C++，则可以使用Mystruct 或Mst
    

使用

**问题**

- 在vector，map里面怎么用

推荐使用上面第4个。

- 是否要new

指针要new，非指针不用new。（new使用堆空间，否则使用栈空间）
