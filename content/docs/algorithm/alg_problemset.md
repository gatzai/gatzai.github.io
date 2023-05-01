+++
title="算法题目集合"
date=2022-11-10
lastmod=2023-04-04T20:16:41.000Z
in_search_index = true

categories = ["算法"]
tags = ["题目"]

[extra]
toc = true
comments = true
+++

算法题目记录，来自leetcode，codeforces

{{< alert icon="mug-hot" cardColor="#FED766" iconColor="#1d3557" textColor="#1d3557" >}}
此文档已经暂停更新
{{< /alert >}}

<!--more-->

## 思维工具：

1. 反向思维（专门用于分析问题），例如：找到 K 个最接近的元素
2. 算法思维：就是那些算法通常用的思维
3. 状态变换思维：比如将某种问题转换为单调状态，能够得出更加高效的方法
4. 递归改为循环，避免了递归过深导致超时，如：1140


## 简单题目

不要小看简单的题目，简单的题目可能有多种解法，去考虑不同的解法，这才是简单题目的价值。

比如：

[https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum/](https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum/)

- 字母与数字

思路：前缀和+哈希表

> https://leetcode.cn/problems/find-longest-subarray-lcci/

- 统计中位数为 k 的子数组

 思路：前缀和+哈希表

> leetcode: 2488

- 在既定时间做作业的学生人数

差分数组可以对应多次查询

[https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/](https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/)

- 找到 K 个最接近的元素

我的思路：双指针，官方的比我的简洁

其他思路：滑动窗口，求这数组的 总和最小的窗口，窗口长度为固定的k。

反向思考：从两端去掉n-k个差最大的。妙啊

[https://leetcode.cn/problems/find-k-closest-elements/](https://leetcode.cn/problems/find-k-closest-elements/)

- 重排序

我的想法总是差那么点意思，是不是我想的太复杂了。

[https://leetcode.cn/problems/shuffle-the-array/](https://leetcode.cn/problems/shuffle-the-array/)

- 验证栈序列

模拟题我就是硬试出来的，把所有的坑都踩了一遍。所以要学习答案的思路啊，好的思路能节省不少时间。

[https://leetcode.cn/problems/validate-stack-sequences/](https://leetcode.cn/problems/validate-stack-sequences/)

- 最大人工岛

细节

[https://leetcode.cn/problems/making-a-large-island/](https://leetcode.cn/problems/making-a-large-island/)

- 最短的桥

[https://leetcode.cn/problems/shortest-bridge/](https://leetcode.cn/problems/shortest-bridge/)

- 雇佣K名工人

花太多时间了！没有把问题想清楚，就凭借印象，活该你花时间找那些逻辑上的错误。

[https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/](https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/)

- 最多能完成排序的块

思路一：前缀和

思路二：取最大下标值

[https://leetcode.cn/problems/max-chunks-to-make-sorted/](https://leetcode.cn/problems/max-chunks-to-make-sorted/)

- 统计有序矩阵中的负数

思路：O(m+n), 使用分治

https://leetcode.cn/problems/count-negative-numbers-in-a-sorted-matrix/

- 第 k 个缺失的正整数

难点：处理边界
这题的处理方法貌似通用

https://leetcode.cn/problems/kth-missing-positive-number/

## 矩阵

- 变为棋盘

毫无思路。。。

可以推出矩阵一定只能包含有两种不同的行，要么与第一行的元素相同，要么每一行的元素刚好与第一行的元素“相反”。用这个结论就可以检测棋盘的合法性。

交换次数就是看变成1，0交替的次数。主意好奇数偶数的区别。

[https://leetcode.cn/problems/transform-to-chessboard/](https://leetcode.cn/problems/transform-to-chessboard/)

- 矩阵快速幂

[https://leetcode.cn/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/](https://leetcode.cn/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/)

- 多米诺和托米诺平铺

思路一：动态规划，主要是难以找出这种状态，并且在短时间内证明是可行的

思路二：根据思路一的dp转移状态，进一步使用矩阵快速幂求解

https://leetcode.cn/problems/domino-and-tromino-tiling/


## 状态压缩
- 获取所有钥匙的最短路径

收集钥匙的过程可能需要返回，所以在某个位置不只是经过一次，所以要对不同的钥匙情况进行记录，这里就用到了状态压缩。

然后是状态要考虑清楚

https://leetcode.cn/problems/shortest-path-to-get-all-keys/

## 递归

* 花括号展开 II

思路：dfs，先找最后的 '}'， 以及在此之前的 '{'，中间部分用逗号分割，三者组合在一起进入下一层 dfs

> leetcode: 1096
## DP动态规划

状态转移！当前状态与上一个状态的关系

- 接雨水（很简单）

[https://leetcode.cn/problems/trapping-rain-water/](https://leetcode.cn/problems/trapping-rain-water/)

- **最少替换次数问题**

方法：动态规划

1. 数组思维
2. 找出不同状态的转换关系

问题类型：最少换几次，才符合某个模式

难点：思路，这题可以用dp，也可以用状态机。但是不管是那种方法，最开始的思维很重要。

[https://leetcode.cn/problems/UlBDOe/](https://leetcode.cn/problems/UlBDOe/)

- 使序列递增的最小交换次数

状态分析

[https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing/](https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing/)

- Good Subarrays

思路是对了，但是没写出转移方程。

[https://codeforces.com/problemset/problem/1736/C1](https://codeforces.com/problemset/problem/1736/C1)

- 粉刷房子

遗传算法？

[https://leetcode.cn/problems/paint-house-iii/](https://leetcode.cn/problems/paint-house-iii/)

- 不同子序列2

妙啊//TODO

[https://leetcode.cn/problems/distinct-subsequences-ii/](https://leetcode.cn/problems/distinct-subsequences-ii/)

- Sending a Sequence Over the Network

dp好题

[https://codeforces.com/contest/1741/problem/E](https://codeforces.com/contest/1741/problem/E)

- 规划兼职工作

思路：按照队尾排序，从小到大dp，利用背包的思路，选择是否取当前时间段的最大值为dp[i], 即dp[i] = max(dp[i-1], dp[i]+pre)

[https://leetcode.cn/problems/maximum-profit-in-job-scheduling/](https://leetcode.cn/problems/maximum-profit-in-job-scheduling/)

- 第n个丑数

思路：丑数仅由2，3，5因子，所以，所有丑数都可以由这几个数构成，将这些数按照特定序列相乘，从小到大，一直算到第n个。

- 最长递增子序列

思路一：暴力, 每次查询以 i 结尾的最长子序列，然后更新 i+1。

思路二：维护一个递增子序列，第i个值表示长度为i的递增子序列的尾数

https://leetcode.cn/problems/longest-increasing-subsequence/solution/

- 数组的均值分割

思路一：动态规划，[参考0-1动态规划](blog/docs/algorithm/alg_template.md)（需要剪枝）

思路二：折半搜索，需要先进行预处理，首先对每个数构造x = x*n-sum，这样平均数为0了，然后在每一半找出两组数使他们和为0即可。最后注意一下不要选取所有。

https://leetcode.cn/problems/split-array-with-same-average/

- 最接近目标价格的甜点成本

思路一：回溯，范围很小，回溯不会很深

思路二：dp，多重背包(直接转换为01背包的做法就行，即可拿多次看成有多个相同的物体)

https://leetcode.cn/problems/closest-dessert-cost/

- 从仓库到码头运输箱子

思路：动态规划+单调队列

https://leetcode.cn/problems/delivering-boxes-from-storage-to-ports/

- N 次操作后的最大分数和

//TODO

> https://leetcode.cn/problems/maximize-score-after-n-operations/

* 石子游戏 II

思路一：模拟+记忆化搜索，关键是要找出合适的状态转移方程，dfs(i,m)表示当前取石头的玩家比另一方多取的石头数

思路二：动态规划，即将递归改为循环

> leetcode:1140

* 多边形三角剖分的最低得分

思路：dp[i][j]表示从点i到点j形成的三角形最小得分，将凸多边形分成三个部分，分别是从i到k，ikj形成的三角形，和k到j。（这里ij应该是三角形的一个边）

> leetcode:1039

## 数位dp

数位DP往往都是这样的题型, 给定一个闭区间[ l , r ], 而这个区间可能很大, 让你求这个区间中满足某种条件的数的总数。

- leetcode 2376
    
    使用dfs深搜每一位
    
- 最大为 N 的数字组合

//TODO

[https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/](https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/)

- 盒子中小球最大数量

https://leetcode.cn/problems/maximum-number-of-balls-in-a-box/

## 序列/字符串

- 交换一次的先前排列

思路：找出最小非递增后缀起点为 i，并找出小于于 i 的且最近的元素 j，两者交换。

> leetcode: 1053

- 分割字符串得到回文串

思路：双指针，on遍历

> leetcode: 1616

- 重建序列

思路：拓扑排序

难点：细节

[https://leetcode.cn/problems/ur2n8P/](https://leetcode.cn/problems/ur2n8P/)

- 有序队列

我的思路：1. 先把最小的放前面，2. 考虑最后一个数，（不行，越想越复杂）

官方思路：这尼玛想不到啊，两种情况：1. k=1，轮盘选择，2. k>1，排序

[https://leetcode.cn/problems/orderly-queue/](https://leetcode.cn/problems/orderly-queue/)

- 非递增顺序的最小子序列

思路：好像是个dp，思路错了就凉凉了，傻逼了，看错题目了

官方思路：贪心+排序，确实简单

[https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/](https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/)

这里拓展一个问题：求第n大的数，O(n)

思路：比我大的放一边，比我小的又放一边，那就知道我是第几大的。就是快排的思路//TODO

[https://leetcode.cn/problems/xx4gT2/](https://leetcode.cn/problems/xx4gT2/)

- 数组中的字符串匹配

思路：暴力，但是评论区有更优解；方法二，拼接字符串，记得加逗号分隔，出现两次说明是

[https://leetcode.cn/problems/string-matching-in-an-array/solution/](https://leetcode.cn/problems/string-matching-in-an-array/solution/)

- 特殊的二进制序列

难点：任意次数，

我的思路：找出所有特殊字串，然后遍历替换，但是没办法处理任意次数

官方思路：把题目看成括号匹配，然后递归，妙啊，不过涉及了很多数学推导，确实难啊。

[https://leetcode.cn/problems/special-binary-string/](https://leetcode.cn/problems/special-binary-string/)

- 尽量少用string操作吧，挺慢的

char数组转换为string，只要给个起始元素的地址就行

[https://leetcode.cn/problems/reformat-the-string/](https://leetcode.cn/problems/reformat-the-string/)

少用string操作，用双指针来解决。

[https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/](https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)

- 最多能完成排序的块 II

我的思路部分和官方法一相同，但是没能处理好重复数字。哇，思路好的话，贼简单。

方法二才是精髓。

[https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/solution/zui-duo-neng-wan-cheng-pai-xu-de-kuai-ii-w5c6/](https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/solution/zui-duo-neng-wan-cheng-pai-xu-de-kuai-ii-w5c6/)

- 最大相等频率

我的思路：先记录所有数字得频率，再记录不同频率得次数，然后从后往前遍历。

我思路和官方差不多，只是没那么优雅。

这题考察得是并列条件，对于多条件得序列，如何把条件写得完备且优雅。其实这题得核心条件就3个，而我考虑太多了。

[https://leetcode.cn/problems/maximum-equal-frequency/](https://leetcode.cn/problems/maximum-equal-frequency/)

- 重复的DNA序列

思路：位运算，滑动窗口

[https://leetcode.cn/problems/repeated-dna-sequences/](https://leetcode.cn/problems/repeated-dna-sequences/)

- 最大交换

有两个思路：空间换时间（室友思路，排序然后从大到小），时间换空间（官方）

[https://leetcode.cn/problems/maximum-swap/](https://leetcode.cn/problems/maximum-swap/)

- 在LR字符串中交换相邻字符

锻炼思维能力吧

[https://leetcode.cn/problems/swap-adjacent-in-lr-string/](https://leetcode.cn/problems/swap-adjacent-in-lr-string/)

- 优势洗牌题

田忌赛马题

[https://leetcode.cn/problems/advantage-shuffle/](https://leetcode.cn/problems/advantage-shuffle/)

- 水果采集

不用滑动窗口会很麻烦

[https://leetcode.cn/problems/fruit-into-baskets/](https://leetcode.cn/problems/fruit-into-baskets/)

- 将 x 减到 0 的最小操作数

思路：滑动窗口

> leetcode:1658

- 分割数组

我的思路：左最大值小于等于右最小值

官方：一次遍历

[https://leetcode.cn/problems/partition-array-into-disjoint-intervals/](https://leetcode.cn/problems/partition-array-into-disjoint-intervals/)

- 最大重复子字符串

我的思路：暴力，一直加字串，直到找不到

进阶思路：序列DP，状态转移：f(i) = f(i-m) + 1，f(i)表示以第 i 个字符结尾的最大重复个数

进阶思路：字符串DP

[https://leetcode.cn/problems/maximum-repeating-substring/](https://leetcode.cn/problems/maximum-repeating-substring/)

- 袋子里最少数目的球

思路： //TODO

> https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/

## 并查集

思路：并查集

难点：为什么要用并查集？用了并查集的性质，能判断两个点是否有同一个根。自己画图模拟一下算法过程就可以很快理解。

并查集，巧妙利用序号来标记同根关系。

冗余连接：[https://leetcode.cn/problems/redundant-connection/](https://leetcode.cn/problems/redundant-connection/)

- 使用负数表示为根，且可以记录数量，妙
- 可能的二分法

//TODO

多种思路

[https://leetcode.cn/problems/possible-bipartition/](https://leetcode.cn/problems/possible-bipartition/)

**字符串**

表达式解析

[https://leetcode.cn/problems/fraction-addition-and-subtraction/](https://leetcode.cn/problems/fraction-addition-and-subtraction/)

- 检查边长度限制的路径是否存在

思路：一边遍历一边加边, 如果 p 和 q 属于同一个集合，则说明存在从 p 到 q 的路径。因为是遍历到小于当前询问值，所以不用判断是否严格小于了，只需要判断是否在同一个集合即可。

> https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/

## 数学

- 使数组和能被 P 整除

思路： 同余

> leetcode: 1590

- 还原排列的最少操作步数

思路：循环链。还有很多其他解法

> leetcode：1806

- 最小差

思路：双指针

难点：超时

[https://leetcode.cn/problems/smallest-difference-lcci/](https://leetcode.cn/problems/smallest-difference-lcci/)

- 集合

交集至少为两个

思路：贪心

难点：不熟悉这种题，但是熟悉后还是挺简单的

[https://leetcode.cn/problems/set-intersection-size-at-least-two/](https://leetcode.cn/problems/set-intersection-size-at-least-two/)

- 最大公约数

辗转相除法，证明余数的最大公约数和其他俩个数一样即可

- 最小公倍数

两数乘积再除以最大公约数

- 使用质因数之和替换后可以取到的最小值

思路：暴力遍历获取质因数

> leetcode:2507

- 快乐数

更优雅的方法：快慢指针，使用快慢指针来判断循环，从而避免使用集合来判断是否有循环

[https://leetcode.cn/problems/happy-number/](https://leetcode.cn/problems/happy-number/)

- 全排列

思路：回溯

难点：思路不要太僵化

[https://leetcode.cn/problems/VvJkup/](https://leetcode.cn/problems/VvJkup/)

- 数组序号排列

思路：排序+哈希表

难点：不熟悉使用哈希表

[https://leetcode.cn/problems/rank-transform-of-an-array/](https://leetcode.cn/problems/rank-transform-of-an-array/)

- 最大回文数乘积 (palindrome)

思路：枚举，枚举一半就行，转换思路就能节约很多时间，而且还是有点细节需要考虑

我的方法，超时，复杂度 O(n*10^2n)，就是这么久

官方：复杂度 O(10^2n)，但其实远小于

[https://leetcode.cn/problems/largest-palindrome-product/](https://leetcode.cn/problems/largest-palindrome-product/)

- 阶乘函数后 K 个零

我的分析：首先只有5与偶数相乘有0，0的数量是递增的。

官方：二分法（二分法的细节，我又忘了，反正最后要么是left=right，要么是left = right-1）

*n! 尾零的数量即为 n! 中因子 10 的个数，而 10=2×5，因此转换成求 n! 中质因子 2 的个数和质因子 5 的个数的较小值。由于质因子 5 的个数不会大于质因子 2 的个数，我们可以仅考虑质因子 5 的个数。*

[https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/](https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/)

- 灯泡开关

群论解法

[https://leetcode.cn/problems/bulb-switcher-ii/solution/by-yun-piao-piao-1-eo7z/](https://leetcode.cn/problems/bulb-switcher-ii/solution/by-yun-piao-piao-1-eo7z/)

**数论**

- 消失的两个数字

思路：异或；或者数分两类

[https://leetcode.cn/problems/missing-two-lcci/](https://leetcode.cn/problems/missing-two-lcci/)

- 第k个数

思路：最小堆；或者多路归并

[https://leetcode.cn/problems/get-kth-magic-number-lcci/](https://leetcode.cn/problems/get-kth-magic-number-lcci/)

- 到达终点数字

脑筋急转弯了

[https://leetcode.cn/problems/reach-a-number/](https://leetcode.cn/problems/reach-a-number/)

**卡特兰数**

- 不同的二叉搜索树

也可以用DP

[https://leetcode.cn/problems/unique-binary-search-trees/](https://leetcode.cn/problems/unique-binary-search-trees/)

**容斥原理**

* 丑数 III

思路：二分+容斥原理

> https://leetcode.cn/problems/ugly-number-iii/

* 序列中不同最大公约数的数目

思路：逆向思维

> leetcode：1819

## 二分

* 有界数组中指定下标处的最大值

思路： 二分法，先假设最大值为 mid，计算出整个数组和，接下来二分。

> leetcode: 1802

## 几何

- 是否为正方形

做法就很多了

1. 我的思路就是先找出直角边，然后推算第四个点是否重合
2. 官方：先用对角线判断平行四边形，再菱形，最后矩形

[https://leetcode.cn/problems/valid-square/](https://leetcode.cn/problems/valid-square/)

- 矩形面积

思路：扫描线，离散化技巧

难，很难理解//TODO

[https://leetcode.cn/problems/rectangle-area-ii/](https://leetcode.cn/problems/rectangle-area-ii/)

## 图

- 细分图中的可到达节点

思路：迪杰斯特拉+找规律

https://leetcode.cn/problems/reachable-nodes-in-subdivided-graph/

- 判断二分图

思路：二分图就是图中的每一条边的两个顶点分别属于不同的集合(仅有两个集合)

https://leetcode.cn/problems/is-graph-bipartite/

- 将节点分成尽可能多的组

思路：每个连通块找到最大的二分图，

https://leetcode.cn/problems/divide-nodes-into-the-maximum-number-of-groups/

## 树

* 统计异或值在范围内的数对有多少

思路：01字典树，每个节点对应一位（0或1）。非常妙啊！首先把计算区间，换成减法，计算异或值小于x的数量。利用01字典树统计（1~j-1）个数的二进制和，在用第j个数与字典树进行比较：当xk为1时，加上dk和jk异或值为0的个数，然后继续搜索异或值为1的下一位；当xk为0时，继续搜索异或值为0的下一位（xk，dk，jk分别表示x的第k位，字典树的第k位，j的第k位）。最后cur.children[bit] 相当于异或为0。

题解里面有一个c++暴力优化AC的，nb。

> leetcode: 1803

- 插入完全二叉树

思路：有空子树的点为待插入点

[https://leetcode.cn/problems/complete-binary-tree-inserter/](https://leetcode.cn/problems/complete-binary-tree-inserter/)

- 最大二叉树

我用了最简单的方法，但是还有更加高效的方法：单调栈，和线段树（看题解）

单调栈：栈内元素单调按照递增(递减)顺序排列的栈，官方例子有点难理解，太巧妙啦，充分利用了遍历的信息 

处理好左右子树的信息很重要，能凭印象写出来，//TODO

[https://leetcode.cn/problems/maximum-binary-tree/](https://leetcode.cn/problems/maximum-binary-tree/)

[https://leetcode.cn/problems/maximum-binary-tree-ii/](https://leetcode.cn/problems/maximum-binary-tree-ii/) （其实就是找规律）

- 移除子树后二叉树的高度

思路1：两边dfs，第一次遍历记录每个节点的高度，使用map<Node, int>结构记录，第二次遍历记录每个节点到根的距离，遍历到某个节点时，取剩余部分树高度（即到根的距离加上同父节点的另一个点的高度）

思路2：dfs序，

[https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/](https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/)

- 最长同值路径

我的思路：以根节点为目标数，两边延申。同理遍历整个树。可以，解决了。n^2

[https://leetcode.cn/problems/longest-univalue-path/](https://leetcode.cn/problems/longest-univalue-path/)

- 统计子树中城市之间最大距离

 题目：寻找子树，子树的直径为 d
 问题：为什么要对子树进行连通性判断？
 思路：

> leetcode: 1617

## 数据结构
**跳表**

难点：跳表的每一个操作的平均时间复杂度是 `O(log(n))`，随机化很巧妙，一定要是均匀随机，不然会超时。

原理很像二叉树

没能自己写出来，这里涉及很多语言细节，需要掌握好。

第二次写，思路会，但是写不出来。。。每一列构成一个节点。

//TODO 希望第三次能够不看答案写

[https://leetcode.cn/problems/design-skiplist/](https://leetcode.cn/problems/design-skiplist/)

**循环队列**

难点：个别特例自己脑子里运行一下，就是细节

思路：你的思路也不是不行，只不过要考虑的情况比较多，稍微复杂了。同样是那么多个变量，官方的思路就很简洁。

[https://leetcode.cn/problems/design-circular-queue/submissions/](https://leetcode.cn/problems/design-circular-queue/submissions/)

**树状数组**

树状数组的构建，从1到n更新C数组，复杂度O(n*logn)

包含方法：

- 求lowbit（二进制最右边的1）：i & -i
- 求前缀和，向前求和
- 更新节点，向后更新

 //TODO

同理算法，求逆序对，这个更好理解。

[https://leetcode.cn/problems/number-of-pairs-satisfying-inequality/](https://leetcode.cn/problems/number-of-pairs-satisfying-inequality/) 

- 求逆序对

树状数组思路：假设数据是从0到n-1（如果不是那也可以用离散化），首先要明白每个节点序号的意思，每个节点的序号表示第几大的数（比如n-1是第1大的数），每次的前缀和表示比此位置大的数的个数。每次获取前缀和后，再更新数组。（当然也可以换一种方式去理解，这里只是用其中一种方法）

**AC自动机**

相关知识：KMP, 字典树

KMP算法适用于单模式串的匹配，而AC自动机适合多模式串的匹配

回顾一下KMP：有两种写法，这里不举例了。

字典树：（数组版）[https://blog.csdn.net/qq_49688477/article/details/118879270](https://blog.csdn.net/qq_49688477/article/details/118879270)

## 有限状态机

- 模糊坐标

我的思路，暴力求解

更严谨的思路，有限状态机

[https://leetcode.cn/problems/ambiguous-coordinates/](https://leetcode.cn/problems/ambiguous-coordinates/)

- 有效数字

## 单调栈&单调队列

内元素单调按照递增(递减)顺序排列的栈

如果是单调递减，就是从原数组中最大的数开始递减，比如从左到右遍历，那么顺序就是：

第一个数：原数组中的最大值，

第二个数：第一个数右边的最大值，

以此类推

如果是单调递增，就是从最小的数开始递增，比如从左到右遍历，那么反之

参考：[https://blog.csdn.net/qq_59144780/article/details/122787827](https://blog.csdn.net/qq_59144780/article/details/122787827)

- 股票价格跨度

思路：单调栈

[https://leetcode.cn/problems/online-stock-span/](https://leetcode.cn/problems/online-stock-span/)

- 和至少为 K 的最短子数组

比较难理解，维护一个单调递增的双端队列  //TODO

[https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/](https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/)

- 所有子数组最小之和

思路：左右单调栈，半开太妙了。除了单调栈，还能用dp

为什么要乘arr[i]，因为是算最小值的和啊。

[https://leetcode.cn/problems/sum-of-subarray-minimums/](https://leetcode.cn/problems/sum-of-subarray-minimums/)

- 下一个更大元素

思路：双单调栈

[https://leetcode.cn/problems/next-greater-element-iv/](https://leetcode.cn/problems/next-greater-element-iv/)

## 综合题目

* 最少翻转操作数

Tag: BFS，并查集，平衡树

思路：首先确定包含 i 的翻转数组的上界和下界，找到规律只能翻转到奇数或偶数位置，然BFS搜索并用并查集记录。

> leetcode: 6365