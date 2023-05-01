+++
title="Matlab使用"
date=2022-11-07
in_search_index = true

categories = ["工具使用"]
tags = ["Matlab"]
[extra]
toc = true
comments = false
+++

## 程序写法

for i=[2 5:9]           %遍历2，5，6，7，8，9

- 函数
    
    function [输出参数列表] = 函数名（输入参数列表）
    
    function [r,s]=rect2polar(x,y)
    
    r=x;
    
    s=y;
    
    end
    

## 数据读取和表示

读取excel

matlab读取Data-EV-demand.xlsx中名为Demand的sheet中E列的数据

[~,~,x]=xlsread('Data-EV-demand.xlsx','Demand')

x(1,1) 表示第一行第一列

- 转成矩阵
    
    要么用内部的导入工具，但是结构是table，还要用table2array
    
    要么用导入函数，有大括号的是元胞数据，使用元胞转矩阵cell2mat
    

- 显示数据
    
    散点图scatter(x, y，‘red’)
    
    折线图plot(x, y)
    
- 显示多个数据：
    - hold on
        
        两个plot之间用一个hold on
        
    - subplot
        
        subplot(2,1,1);plot(y1);
        
        subplot(2,1,2);plot(y2);
        

元胞：元胞的元素可以说数字，字符，矩阵，字符串，是一个元素多元化的矩阵

元胞置空cell(1:1)=[];

## 数据处理

x. 是做矩阵元素做运算

x 是矩阵整体做运算

x.’是转置

x’是共轭转置，共轭就是矩阵每个元素都取共轭（实部不变，虚部取负）

- unifrnd

生产均匀随机数

unifrnd(a, b, [m, n])，产生a，b范围内均匀分布的的m*n数组

- normrnd

生成服从正态分布的随机数

R＝normrnd(MU,SIGMA,m,n)  %m是个数，n是组数

- sum

sum内部可以用一个范围量

比如：sum（x < 5) ，这里是求数组x中小于5的元素的个数

- linprog

求最小值

linprog(目标函数中的系数，不等式左边系数，不等式右边系数，[]，[]，下界，[])

- linspace

x=linspace（1，100，3）

- repmat

扩充矩阵

行扩充2倍，列扩充3倍：repmat(a, 2, 3)

- min和max

min对矩阵来说是求每一列的最小值，结果是1行m列

### 数学

求二次规划：

**quadprog**

x = quadprog(H,f,A,b)

A与b是小于等于约束，A是系数，b是常数 

H与f是函数，$\frac{1}{2}x^THx+f^Tx$

目的是找满足约束的最小值

s输出是：x的最小值，与结果fval

[https://blog.csdn.net/weixin_42985452/article/details/120628996](https://blog.csdn.net/weixin_42985452/article/details/120628996)