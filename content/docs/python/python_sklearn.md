+++
in_search_index = true
title="Sklearn使用"
date=2022-11-08

[taxonomies]
categories = ["工具使用"]
tags = ["Python","sklearn","机器学习"]
[extra]
toc = true
comments = false
+++

### 注意

新版sklearn中，所有数据都应该是二维矩阵，哪怕它只是单独一行或一列，需要使用.reshape(1,-1)进行转换

### 分类

svm.SVC()

clt.fit(X, y)

- 分类前最好做标准化处理

$a_{ij} = \frac{a_{ij} - \mu j}{\sigma_j}$ ， j = 0 → 指标数，注意：标准差和均值都是用已分类的数据所求的，对未知数据和已知数据都要标准化

- 核函数

svm.SVC(kernel='linear')  #线性

svm.SVC(kernel='poly', degree=3) #多项式

svm.SVC(kernel='rbf') #非线性

svm.SVC(kernel='sigmoid') #S型

### 回归

svm.SVR()

clf.fit(X, y)

- 逻辑回归
    
    clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6, solver='liblinear')  #初始化
    
    clf.fit(X, y) #输入数据训练
    
    clf.predict(data) #进行预测
    

> 参考：[https://blog.csdn.net/m0_53907018/article/details/119948867](https://blog.csdn.net/m0_53907018/article/details/119948867)
> 

### 归一化

- 最大最小

```py
min_max_normalizer=preprocessing.MinMaxScaler(feature_range=(0,1))     

#feature_range设置最大最小变换值，默认（0,1）
scaled_data=min_max_normalizer.fit_transform(data)    

#将数据缩放(映射)到设置固定区间，如果data是numpy格式的数据，数据结构需要是（n, 1），不能是（n，），所以要用reshape(-1, 1)，但也可以将data转为DataFrame，处理更简单。结果scaled_data就已经可以用了
```

### 标准化

- Z-Score

资料标准化后会使每个特征中的数值平均变为0(将每个特征的值都减掉原始资料中该特征的平均)、标准差变为1

- scale

price_frame=pandas.DataFrame(data)

normal_data=preprocessing.scale(price_frame)

- scale 和 StandardScaler
    - scale 只能分开使用
    - StandardScaler 可以同时用与训练集和测试集（相当于在训练集上用完后，可以直接将训练集导入，因为假设训练集的期望和测试集的期望是一样的）
        
        比如：
        
        scaler = preprocessing.StandardScaler().fit(X_train)
        
        scaler.transform(X_test)
        

> [https://blog.csdn.net/weixin_46031067/article/details/118767432](https://blog.csdn.net/weixin_46031067/article/details/118767432)
> 

### KFold
```py
from sklearn.model_selection import KFold
#KFold(n_splits=’warn’, shuffle=False, random_state=None)
# 参数
# n_splits 表示划分为几块（至少是2）
# shuffle 表示是否打乱划分，默认False，即不打乱
# random_state 表示是否固定随机起点，Used when shuffle == True.

# 方法 
# get_n_splits([X, y, groups]) 返回分的块数 
# split(X[,Y,groups]) 返回分类后数据集的index，它是用于对X进行划分，返回的是他们的索引值。由于是将data set划分成两部分，所以返回的值有两个。一个是训练集，一个是验证集。

x = np.array([[1,2], [3,4],[5,6],[7,8],[9,10],[11,12]]) +10
y = [i+21 for i in range(4)]
kf = KFold(n_splits=3)
print(kf.get_n_splits(x))
# 输出： 3
	
for train_i, test_i in kf.split(x):
	print(train_i, test_i)
	print('---')
# 输出：
'''
[2 3 4 5] [0 1]
---
[0 1 4 5] [2 3]
---
[0 1 2 3] [4 5]
---
'''
```

### StratifiiedKFold

### 交叉验证

```py
from sklearn.model_selection import cross_val_score
# 参数
# estimator:估计方法对象(分类器)模型
# X：数据特征(Features)
# y：数据标签(Labels)
# cv代表分成几折，cv数值最大 = 数据集总量的1/3
# scoring 评估效果
# sklearn.cross_validation.cross_val_score(estimator, X, y=None, scoring=None,cv=None, n_jobs=1, verbose=0, fit_params=None, pre_dispatch=‘2*n_jobs’)

scores = cross_val_score(svc, data, y_label, cv=5)
print(scores)

```

关于 scoring 评估效果参数的解释，
| 取值 |	含义|
| -- | -- |
| ‘accuracy’ |	准确度
| ‘precision’ |	精度
| ‘f1’ |	f1_score对于二进制目标
| ‘f1_micro’ |	微观F1
| ‘f1_macro’ |	宏F1，二分类使用Accuracy和F1-score，多分类使用Accuracy和宏F1。
| ‘recall’ |	召回率
| ‘roc_auc’ |	AUC值
| neg_log_loss |	neg_log_loss损失，结果越接近0，表示损失越小，模型效果越好,对数似然函数 Log_loss是一种直接根据概率预测结果衡量损失的函数，和逻辑回归中的损失函数类似。对数似然函数直接指向模型最优化方向，对于那些以最优化为目的求解模型的算法来说，会天然有较好的得分。比如逻辑回归、svm等，其中逻辑回归的损失函数就是对数似然。
| ‘r2’ |	R方，越大越好,R^2可以为负
| neg_mean_squared_error |	负均值平方误差，负数，越小越好，均方误差MSE的数值，其实就是neg_mean_squared_error去掉负号的数字
| neg_mean_absolute_error |	负绝对均值误差，MAE的负取值，现实中MSE和MAE选一个来使用就好了

> https://blog.csdn.net/worther/article/details/126909270
> https://zhuanlan.zhihu.com/p/509437755

### RandomForestRegressor

参数

- criterion
- n_estimators
- oob_score

> [https://blog.csdn.net/xiaohutong1991/article/details/108178143](https://blog.csdn.net/xiaohutong1991/article/details/108178143)
> 

**数据处理**

train_test_split(train_data, train_target, test_size=0.25,stratify=y) #随机划分测试集和训练集

参数：

test_size：测试集样本数目与原始样本数目之比

将stratify=X就是按照X中的比例分配，将stratify=y就是按照y中的比例分配

### 产生数据集

- make_classification
    
    单标签分类生成器
    
    **用法**
    
    from sklearn.datasets import make_classification
    
    X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
    
    **参数**
    
    n_samples, 需要的数据
    
    n_classes,分类数量，默认为2
    
    n_features, 数据的特征量数，数据是一列还是几列
    
    n_redundant, 具有其它特征量的额外数据量
    
    random_state, 随机数种子
    

- make_blobs
    
    常被用来生成聚类算法的测试数据，直观地说，make_blobs会根据用户指定的特征数量、中心点数量、范围等来生成几类数据，这些数据可用于测试聚类算法的效果
    
    **用法**
    
    from sklearn.datasets import make_blobs
    
    X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=0)
    
    参数
    
    - **n_samples**是待生成的样本的总数。
    - **n_features**是每个样本的特征数。
    - **centers**表示类别数。
    - **cluster_std**表示每个类别的方差，例如我们希望生成2类数据，其中一类比另一类具有更大的方差，可以将cluster_std设置为[1.0,3.0]。

- 内置数据集
    
    鸢尾花数据集：load_iris
    
    乳腺癌数据集：load_breast_cancer
    
    使用说明：
    
    若直接返回，则数据集属性data为数据，feature_names为属性名，target为类别
    
    若加参数return_X_y=True，这个参数表明返回值为X， y
    

参考

> [https://www.cnblogs.com/hider/p/15978785.html](https://www.cnblogs.com/hider/p/15978785.html)
