+++
in_search_index = true
title="Pandas使用"
date=2022-11-08
lastmod=2023-02-17

[taxonomies]
categories = ["工具使用"]
tags = ["Python","pandas","数据处理"]
[extra]
toc = true
comments = false
+++

## 理解数据

---

1. 查看数据属性，data.info()

### 读取csv

```python
data = pd.read_csv('monthly-sunspots.csv',names=['Month','Sunspots'])
```

解释：读取monthly-sunspots.csv，其中有两列，分别是：Month和Sunspots

参数：

skiprows=4 #跳过前4行，或skiprows=[0,1,2,3]

sheet_name=“sheetname”#指定sheet

### 提取行与列

```python
train_sunspots = data.iloc[1:20,:]
```

解释：提取1到20行，以及所有列

- loc
    
    data.loc[行索引, 列名] = val
    
    data.loc[行索引] = val
    
    loc和at的区别：loc可以取多个值，at只能取一个格子里面的值

- 索引标签 

    单列：df["col_a"]
    多列：df[["col_a","col_b"]]

**转为numpy**

- to_numpy()
- 直接用values，df.values

### 数据类型转换

- 首先显示类型，用来确认类型：data.dtypes
- 然后将里面的Sunspots数据转为float：test = data.Sunspots.astype(float)

原函数

```python
df.astype(dtype, copy:bool=True, errors:str=‘raise’)
```

- Series 转dataframe
    1. 使用构造函数
    2. to_frame
- 转为字典
    
    df.to_dict(orient="records")
    

### 查看数据的结构

pandas包含两种最主要数据结构：序列（Series）和数据框（DataFrame）。对于这两个数据结构，有两个最基本的概念：轴（Axis）和标签（Label），对于二维数据结构，轴是指行和列，轴标签是指行的索引和列的名称，存储轴标签的数据结构是Index结构。

获取标签：df.columns.values

重新命名标签：

`df.columns = ['a', 'b', 'c', 'd']`

`df.columns = df.columns.str.replace('a', 'b')`

* 输出所有项目

在控制台 print 时，过长的输出一般都会显示省略号，但如果要强制看所有内容，可以用以下方法

```py
#显示所有列
pd.set_option('display.max_columns', None)

#显示所有行
pd.set_option('display.max_rows', None)
```

## 数据获取与统计

---

- 使用正则
    
    df.filter
    
- value_counts()
    
    统计不同数据得个数
    
- truncate
    
    df.truncate(before=2,after=4)  #截取索引 2-4 （包括）之间的数据
    
- rolling
    
    r = df.rolling(window = 10) #滑动窗口
    
    r.mean() #算窗口的均值。。。
    
- 统计空数据的个数

    df.isnull().sum()

- 获取数据切片

    df[ df['a'] == 'v1' ] #获取标签为 ‘a’ 列中值为 ‘v1’ 的那一行数据

- 获取小于某值的数据

```python
def smaller(x):
    return x < 10
df[df['xxx'].apply(smaller)] #筛选小于10的数

def two_smaller(x):
    mins = min(x[0], x[1])
    return mins,mins
#多列apply
df[['c1', 'c2']].apply(lambda x:two_smaller(x), axis=1)
```

## 数据删除

---

- drop
    
    ```py
    df= df.drop('column_name', 1)
    #参数解释：
    #labels：待删除的行名or列名
    #axis：删除时所参考的轴，0为行，1为列；
    #inplace：布尔值，默认为False,这是返回的是一个copy;若为True,返回的是删除相应数据后的版本
    ```

    
    删除前三行：`df.drop(index=[0,1,2])`
    
- df.dropna(inplace=True)
    
    删除空数据，注意，空数据删除后，index也会删除

- 删除重复数据

    df.duplicated()  #构建重复数据的series结构，重复为True
    
    df.duplicated(["xx"]) #指定列

    df.drop_duplicates(["xx"]) #去除重复，并返回去除后的结构



## 数据处理

---

- 一阶差分
    
    diff
    
- 数据偏移
    
    shift
    

### 数据拼接

三种merge，join，concat

[https://m.jb51.net/article/245194.htm](https://m.jb51.net/article/245194.htm)

- concat
    
    concat([arr1, arr2], axis=0) #axis=0 行数相加， axis=1 列数相加
    
- join

    pd.merge(left, right, how='', on='index')
    #how 有四种，
    * left：保留左表的index
    * right：保留右表的index
    * inner：保留两个表相同的index
    * outer：保留两个表所有的index

    #on: 指定主键列

**定义dataframe**

```python
df = DataFrame([
('虎子', 5, "dog"),
('老许', 3, "bird"),
('二赖子', 6, "fish"),
('老白', 8, "catty"),
('小黑', 10, "puppy"),
],
columns=('name', 'age', 'class')
)
```

### 计算

* 求和

```py
data['col1'].sum() #列 col 求和
data[['col1']].sum(axis=0) #同上
data[['col1','col2']].sum(axis=1) #对 col1 和 col2 每一行求和
```
> https://www.jianshu.com/p/79cf14bb0b33

* 求均值

```py
df.mean() #每一列的均值
df['col'].mean() #每 col 列的均值
```

* 插值

可用于空值用上下值的平均值填充
```py
#参数
#axis ： 沿哪个轴进行
#limit ： 整数，要填充的连续NaN的最大数量
df['col1'] = df['col1'].fillna(df['col1'].interpolate())
```

### 替换数据

df.replace(to_replace, value)

replace({'-': None},inplace =True)  #替换为空

正则替换：df.replace([oldA, oldB],[newA, newB])

替换 nan : df['x'].fillna(0) #把标签为 ‘x’ 的数据中的 nan 替换为 0 。

### 批处理apply

所有数据开方：df.apply(np.sqrt)

lambda处理：df.A = df.A.apply(lambda x:x+1)

lambda去空格:

```python
def fun_str(x):
    return(''.join(x.split()))
    
df["xx"]=df["xx"].astype(str).apply(lambda x:fun_str(x))
```

### 数据离散化

将离散型特征的每一种取值都看成一种状态，若你的这一特征中有N个不相同的取值，那么我们就可以将该特征抽象成N种不同的状态

```python
s = pd.Series(list('abca'))
print(pd.get_dummies(s)) #三个离散值
#即
'''
	 a  b  c
0  1  0  0
1  0  1  0
2  0  0  1
3  1  0  0
'''

df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
print(pd.get_dummies(df))
#即
'''
	 C  A_a  A_b  B_a  B_b  B_c
0  1    1    0    0    1    0
1  2    0    1    1    0    0
2  3    1    0    0    0    1
'''
```

参考：[https://zhuanlan.zhihu.com/p/139144355](https://zhuanlan.zhihu.com/p/139144355)

### 时间数据

```py
date_range(
    start=None, 
    end=None,
    periods=None, #指定生成时间序列的数量
    freq=None, #生成频率，默认‘D’，可以是’H’、‘D’、‘M’、‘5H’、‘10D’
    tz=None,
    normalize=False,
    name=None,
    closed=None, #是否包含开始和结束时间，left 包含开始时间，不包含结束时间，right 与之相反，默认同时包含开始时间和结束时间
    **kwargs)
#时间形式：
# 1. 01/01/2020
# 2. 20200101
# 3. 2020-01-01

pd.date_range('2020-01-01', periods= 4) #往后生成4天，即 01 号到 04 号。
pd.date_range('2020-01-01', '2020-01-04') #生成两个日期之间，包括起始和结尾

#获取所有天数
print(date.day.values)
#获取所有小时
print(date.hour.values)
#其他同理


```

## 显示数据

---

- 显示少数离散数据的数量
    
    df.Pclass.value_counts().plot(kind='bar')         #df里面有Pclass属性的数据
    

- 显示两种数据，比如数据sex在数据survived里面的比重
```python
    survived_m = train_data.Survived[train_data.Sex == 'male'].value_counts()   #统计男性存活与否的数量
    survived_f = train_data.Survived[train_data.Sex == 'female'].value_counts()
    df = pd.DataFrame({'male':survived_m, 'femal':survived_f})
    df.plot(kind = 'bar', stacked=True)    #stacked 堆叠形式
```
