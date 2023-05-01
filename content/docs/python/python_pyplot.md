+++
in_search_index = true
title="Pyplot使用"
date=2022-11-08

[taxonomies]
categories = ["工具使用"]
tags = ["Python","pyplot","可视化"]
[extra]
toc = true
comments = false
+++

## 基础
**标签打竖**

plt.xticks(rotation=270)

**显示线段图**

plt.plot(train_sunspots, label="Training Data")

**多张图**

plt.subplot(n,m,p)  #有n行，m列，显示在第p个

plt.plot(…)

plt.show()

**中文**

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

**尺寸**

`plt.figure(figsize**=**(9,6))`

**x，y轴长度相同**

plt.xlim(-0.2, 0.2)
plt.ylim(-0.2, 0.2)

## 各种类型图

### KDE图

plot(kind='kde')

不知道是个什么j8图

### 等高线图

ax.contourf(x, y, z)

参数：

cmap=plt.cm.coolwarm #色调

### 热力图
```python
cmap = plt.cm.get_cmap('coolwarm', 1000)#plt.cm.hot
plt.imshow(cor, cmap=cmap, vmin=-1, vmax=1)
plt.colorbar()
```

[配色参考](https://blog.csdn.net/KIKI_ZSH/article/details/123505175)

## 其他

[结合pandas显示数据](@blog/docs/python/python_pandas.md)