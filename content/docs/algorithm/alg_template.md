+++
title="算法题目模板"
date=2022-11-10
updated=2023-03-21T22:55:48.000Z
in_search_index = true

categories = ["算法"]
tags = ["模板"]

[extra]
toc = true
comments = false
math = true
+++

## 字符串哈希模板
一般来说，我们取P=131或P=131313，等质数，此时Hash值产生冲突的概率极低，

哈希数组：h[i] = h[i-1]*P + str[i-1];

次方数组：p[i] = p[i-1]*P;

子串哈希：

int hash = h[j] - h[i - 1] * p[j - i + 1];

- 为什么要乘次方数组？
    
    保持位数相等，防止相减错误，即将P的次方量级保持相等
    
    $h[i] = \sum ^{i-1}_{k=0} c_k P^{i-k-1}$ 
    
    $p[i] = P^i$
    
    可得 $h[j] - h[i - 1] * p[j - i + 1] = ( \sum ^{j-1} _{k=0} c_k P^{j-k-1}-\sum \limits ^{i-2} _{k=0} c_k P^{j-k-1})$  ，好像得到了一个更难的公式了。
    

例题：

找字符串中特定长度的子串，数量大于1个的子串

[https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247489813&idx=1&sn=7f3bc18ca390d85b17655f7164d8e660](https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247489813&idx=1&sn=7f3bc18ca390d85b17655f7164d8e660)

## 单调栈模板
构建最大二叉树：最大数的左边是左子树，右边是右子树，如此递归构造

```cpp
//nums 是节点数组
int n = nums.size();
vector<int> stk;
vector<int> right(n, -1), left(n, -1);
//vector<TreeNode*> nodes(n);
for(int i=0; i<n; ++i)
{
    //nodes[i] = new TreeNode(nums[i]);
		//标记左子树：将小于当前元素的值设为左子树
    while(!stk.empty() && nums[stk.back()] < nums[i]) 
    {
        right[stk.back()] = i;  // right[a] = b; 意味着序号a是序号b的左子树
        stk.pop_back();
    }
		//标记右子树：由于左子树在上一步已经标记完成了，所以只需要再标记一次右子树
    if(!stk.empty())
    {
        left[i] = stk.back(); // left[a] = b; 意味着序号a是序号b的右子树
    }
    stk.emplace_back(i);
}

//后面根据right和left的情况来构建这颗二叉树（以下只是看着程序叙述，并不一定好理解，如果以后需要理解，请重新表述）
/*
1. left 和 right 都为-1的时候，则此点为根
2. right 为 -1， 或者 left不为-1且 left对应的值小于right对应的值，则此点是left对应的节点的右子树
3. 其余情况为 此点是 right对应的节点的左子树
*/

```

- 单调递增栈（存储下标）
    
    遍历规则：（一轮操作）若当前元素值小于栈顶，则弹出，直到栈顶大于当前元素
    
    一轮操作完后，栈顶表示左侧比当前元素要小的下标
    
    然后压入当前元素，继续遍历下一个。
    
- 单调递减栈（存储下标）
    
    栈顶表示比当前元素要大的下标(非严格)
    
- 进阶
    
    单调栈不仅可以存储左侧最值，还可以算出右侧最值信息。

	* 严格单调增栈，左边找小于的值，右边找小于等于的值

	* 严格单调减栈，左边找大于的值，右边找大于等于的值

	* 非严格单调增栈，左边找小于等于的值，右边找小于的值

	* 非严格单调减栈，左边找大于等于的值，右边找大于的值。栈顶就是左边第一个比它大或等于的数，当前元素是出栈的数右边第一个比它大的数。代码如下：

	```cpp
	{
		vector<int> nums(N);
		vector<int> stk;
		//lr[i].first 是左边大于等于第i个数的下标，lr[i].second是右边...的
		vector<pair<int,int>> lr(N, {-1,-1});
		for(int i=0; i<N; ++i)
		{
			//非严格递减栈，（入栈前）获取左边大于或等于当前元素的下标，
			//(出栈时)当前元素就是右边大于出栈元素的第一个值
			//栈递减还是递增，用这个比较符号来判断
			while(!stk.empty() && nums[i] > nums[stk.back()])
			{
				lr[stk.back()].second = nums[i];
				stk.pop_back();
			}
			lr[i].first = stk.empty() ? -1 : nums[stk.back()];
			stk.push_back(i);
		}
	}
	```

## 树状数组模板


```cpp
	vector<int> tree;
	// 求最低位1
  int lowbit(int i)
  {
      return i&-i;
  }
	
	//向后更新
  void update(int p)
  {
      int n = tree.size();
      for(;p < n; p+=lowbit(p))
          ++tree[p];
  }
	
	//统计前缀和
  long long tsum(int p)
  {
      long long res = 0;
      int n = tree.size();
      for(;p >= 1; p-=lowbit(p))
          res += tree[p];
      return res;
  }
```

> [https://leetcode.cn/problems/number-of-pairs-satisfying-inequality/](https://leetcode.cn/problems/number-of-pairs-satisfying-inequality/)
> 

### 二维树状数组

```cpp
int n, m;
ll mat[5000][5000];

int lowbit(int i) {
    return i & -i;
}

long long tsum(int x, int y) {
    ll res = 0;

    for (int i = x; i >= 1; i -= lowbit(i))
        for (int j = y; j >= 1; j -= lowbit(j)) {
            res += mat[i][j];
        }

    return res;
}

void update(int x, int y, int value) {
    for (int i = x; i <= n; i += lowbit(i)) {
        for (int j = y; j <= m; j += lowbit(j)) {
            mat[i][j] += value;
        }
    }
}

//区域c 到 a， d 到 b， 闭区间
ll section_sum(int a, int b, int c, int d) {
    ll ans = tsum(c, d) - tsum(a - 1, d) - tsum(c, b - 1) + tsum(a - 1, b - 1);
    return ans;
}
```

> [https://loj.ac/p/133](https://loj.ac/p/133)
>

## 并查集模板
```cpp
//原始版本
int uf_find(vector<int>& parent, int a)
{
	if(parent[a] != a)
		parent[a] = uf_find(parent, parent[a]);
	return parent[a];
}

void uf_union(vector<int>& parent, int from, int to)
{
	parent[uf_find(parent,from)] = uf_find(parent,to);
}


//-1版本，正数表示下标，负数表示个数
int uf_find(vector<int>& parent, int a)
{
	//找到负数的前一个
	return parent[a] < 0 ? x : parent[a] = uf_find(parent, parent[a]);
}

void uf_union(vector<int>& parent, int a, int b)
{
	int p1 = uf_find(parent,b);
	int p2 = uf_find(parent,a);
	if(p1 != p2)
	{
		parent[p1] += parent[p2];
		parent[p2] = p1;
	}
}
```

## 数位dp模板
```cpp

string s;
int dp[10][1<<10][2][2];
int dfs(int p, int mask, int limit, int zero) {
	if (p == s.size()) return 1-zero;//全是前导零则不算答案。前导零，即前面全为0。zero=1，表示之前是前导零
	if (dp[p][mask][limit][zero] != -1) return dp[p][mask][limit][zero]; //遇到计算过的状态直接返回
	int res = 0;
	// 累计前导零的方案数
	// zero=1，limit=1,由于之前是存在前导零，所以构造的位数必定小于n的位数，第p+1位最多能取到9;
	// 现在也是填充0，所以第p+1位的zero=1
	if (zero == 1) res += dfs(p+1, mask, 0, 1);
	// 累计非前导零的方案方案数
	// 枚举的下限取决于zero。
	//      当存在前导零，由于当前统计非前导零的方案数，所以只能从1开始
	//      若不存在前导零，当前从0开始构造是可以满足最终构造的数<=n的枚举上限取决于limit。
	//      当limit存在说明p之前构造的数恰好是n的前缀，此时若超过n的第p位则不满足最终构造的数<=n。
	//      当limit不存在说明前p位构造的数已经在字典序上小于n的前p位了，第p位即使取9，最终构造的数也不会大于n
	for (int i=(zero?1:0); i<=(limit?s[p]-'0':9); i++) 
	{
		// 不设置当前位为前导零，若之前为前导零则当前可从0开始，否则是1，若limit存在当前值超过s[p]必定大于n
    if (mask>>i&1) continue; //前p个构造的数中已经有i，跳过。
    res += dfs(p+1, mask|1<<i, limit&&(i==s[p]-'0'), 0);
    // limit = limit&&(i==s[p]-'0'), 当前p个数是n的前缀，且第p个数也取到了n的第p位则形成了长度为p+1的前缀
    // zero = 0, 当前循环是统计非前导零的方案数。
	}
	return dp[p][mask][limit][zero] = res;
}

int countSpecialNumbers(int n) 
{
	s = to_string(n);
	memset(dp, -1, sizeof(dp));
	return dfs(0, 0, 1, 1);
	//limit=1，第一位的最大值最多不能超过s[0],否则大于n.
	//zero=1，前导零存在后续的前导零才可以存在
}
```

原理：相当于遍历每一个有效数字位，每一位都存储起来，所以对于重复的数只会算到下一级，而不会一直算到底层。
（比如：2345，第0位是2，第一位是3，以此类推，如果已经已经算过第四位的10位数，即0->0->0->[0-9]，那么当遍历到第二位的1时，只需要看一下第三位记录的数即可）

时间复杂度为：O（logN）

```cpp
//问题：统计0~n中，数字1出现的个数
int bit_dp(int n) {
    auto s = to_string(n);
    int m = s.length(), dp[m][m];
    memset(dp, -1, sizeof(dp));
    function<int(int, int, bool)> f = [&](int i, int cnt1, bool is_limit) -> int {
        if (i == m) return cnt1;  //统计到个位的后面 （个位是m-1）
        if (!is_limit && dp[i][cnt1] >= 0) return dp[i][cnt1];  //(1)
		//zeros
        int res = 0;
        int up = is_limit ? s[i] - '0' : 9;  //显然从最高位开始limit
        for (int d = 0; d <= up; ++d) // 枚举要填入的数字 d
            res += f(i + 1, cnt1 +(d==1), is_limit && d == up);
        if (!is_limit) dp[i][cnt1] = res;  //在limit上不能统计，(2)
        return res;
    };
    return f(0, 0, true);
}
//当 i = 0 表示 n 的最高位

/*
对于（1）（2）不理解的话可以这么想：
另 n=234, 有 m = 3，
如果去除（1）和（2），那么相当于遍历 0 到 234。加上（1）和（2）只是减少了重复遍历的情况。

（1）中的if相当于得到记录了每一位上所有非limit的答案，所以不需要重复遍历了直接返回即可。
（2）中的if相当于记录非 limit 情况下，第 i 位 0~9 的答案。

那么为什么只需要非 limit 的呢，因为对于 n=234
在十位上，0，1，2是非limit，所以这三者的答案一样，所以只需要记录一次，后面直接返回即可。而3是limit，所以需要遍历。

可得limit和非limit答案也是不一样的，所以做出区别。

为什么一开始 0 是 limit。
因为最高位必然有限制，不一定遍历到 9 。
*/
```

```python
# 问题：至少有 1 位重复的数字
# 使用 @cache 能够简化 01dp 模板
def numDupDigitsAtMostN(self, n: int) -> int:
	s = str(n)
	m = len(s)
	@cache
	def f(i, dup, mask, is_limit):
		if i == m:
			if dup:
				return 1
			return 0
		ans = 0
		up = int(s[i]) if is_limit else 9
		for d in range(up+1):
			mask2 = mask if mask == 0 and d == 0 else mask | (1<<d)
			dup2 = dup or (mask & (1<<d))
			ans += f(i+1, dup2, mask2, is_limit and d == up)
		return ans
	return f(0, False, 0, True)
```

参考：

> [每一位不相同数的个数](https://leetcode.cn/problems/count-special-integers/solution/shu-wei-dp-mo-ban-by-endlesscheng-xtgx/)
[数字1的个数](https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/solution/by-endlesscheng-1egu/)

## 背包问题

* 0-1背包问题：每个元素最多取1次
```cpp
dp[0] = 1;
for(int num : nums) {
	for(int i = target; i >= num; i--) {
		dp[i] |= dp[i - num];	//遍历每个元素，如果选择该元素则在其他已选的元素后加上该元素。
	}
}
//dp[target] == 1 表示元素能够合成target
```
* 完全背包问题：每个元素可以取多次
* 多重背包问题：每个元素数量都不同

## 线段树
一棵二叉树，节点是存储区间[l, r]中某个需要的值。

4倍空间，

```cpp
ll a[N];

struct Seg
{
	int l, r;
	ll val, tag;  //tag是懒标记
}seg[N<<2];

void push_up(Seg& u, const Seg& l, const Seg& r)
{
	u.val = max(l.val, r.val);   //比如说求最大值
	//u.val = l.val + r.val;   //比如说区间和
}

void push_down(Seg& u, const Seg& l, const Seg& r)
{
	l.val += u.tag * (l.r - l.l+1);
	l.tag += u.tag;

	r.val += u.tag * (r.r - r.l+1);
	r.tag += u.tag;
	u.tag = 0;
}

//建树，id=1，l左边界，r右边界
void seg_build(int id, int l, int r)
{
	seg[id].l = l;
	seg[id].r = r;
	if(l == r)
	{
		seg[id].val = a[l];  //a为原来数组，seg是线段树
		return ;
	}
	int m = l+r>>1;
	seg_build(id << 1, l, m);  //左子树
	seg_build(id << 1|1, m+1, r);  //右子树
	push_up(seg[id], seg[id<<1], seg[id<<1|1]);  //更新父节点
}

//更新
void seg_update(int id, int l, int r, ll val)
{
	if(l <= seg[id].l && seg[id].r <= r)
	{
		seg[id].val += val * (seg[id].r - seg[id].l +1);
		seg[id].tag += val;
		return;
	}
	push_down(seg[id], seg[id<<1], seg[id<<1|1]);
	int m = seg[id].l + seg[id].r >> 1; //先加再右移
	if(l <= m)seg_update(id<<1, l, r, val);
	if(m < r)seg_update(id << 1|1, l, r, val);
	push_up(seg[id], seg[id<<1], seg[id<<1|1]);
}

//查询，id为当前区间下标
ll seg_query(int id, int l, int r)
{
	if(l <= seg[id].l && seg[id].r <= r)
	{
		return seg[id].val;
	}
	push_down(seg[id], seg[id << 1], seg[id << 1|1]);
	ll rt = 0;
	int m = seg[id].l + seg[id].r >> 1;
	if(l <= m)rt += seg_query(id<<1, l, r);
	if(m < r)rt += seg_query(id << 1|1, l, r);
	return rt;
}

void seg_print()
{
	for(int i=1; i<(N<<2); ++i)
	{
		if(seg[i].l != 0)
			cout << "id:" << i << "[" << seg[i].l << "," <<\ 
			seg[i].r << "] val:" << seg[i].val << "tag:" <<\
			seg[i].tag << endl;
	}
}
```

> [https://www.cnblogs.com/xenny/p/9801703.html](https://www.cnblogs.com/xenny/p/9801703.html)


## 离散化
对于数据范围大，但是数据量较少的。不能直接申请太大的数组，需要做离散化。

## 矩阵前缀和
```cpp
vector<vector<int>> arr(nr, vector<int>(nc, 0));
for(int i=1; i<=nr; ++i)
{
    for(int j=1; j<=nc; ++j)
    {
        arr[i][j] = arr[i][j-1] + mat[i-1][j-1] + arr[i-1][j] - arr[i-1][j-1];
    }
}
//arr[i][j] 表示子矩阵mat[0-i][0-j]所有元素和
```

## 树

用边信息构建树的模板
```cpp
long long minimumFuelCost(vector<vector<int>>& roads, int seats) {
        int n = roads.size()+1;
        vector<vector<int>> arr(n, vector<int>());
        for(auto& a:roads)
        {
            arr[a[0]].push_back(a[1]); 
            arr[a[1]].push_back(a[0]); 
        }
        long long ans = 0LL;
        function<int(int,int)> dfs = [&](int s, int fa) {
            int ret = 1;
            for(auto& v: arr[s])
            {
                if(v!=fa)
                {
                    int t = dfs(v, s);
                    ans += (t+seats-1)/seats; //t/seats向上取整
                    ret += t;
                }
            }
            return ret;
        };
        dfs(0,-1);
        return ans;
    }
```
> https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/

### 主席树

主席树的经典应用在于求某个区间内的第K小/大数的值。

前置知识为线段树。

### 树的直径

计算树的直径长度有常见的两种方法:

1. 动态规划：我们记录当 root 为树的根时，每个节点作为子树的根向下，所能延伸的最远距离 d1 和次远距离 d2 ，那么直径的长度就是所有 d1 + d2 的最大值。

	```python
	maxlen = 0
	dp1, dp2 = [0]*4, [0]*4
	def dfs_dp(start, f):
	    dp1[start] = dp2[start] = 0
	    for i in tree[start]:
	        if i == f: continue
	        dfs_dp(i, start)
	        t = dp1[i] + 1
	        # dp1记录第一大的值，dp2记录第二大的值
	        if t > dp1[start]:
	            dp2[start] = dp1[start]
	            dp1[start] = t
	        elif t > dp2[start]:
	            dp2[start] = t
	    global maxlen
	    maxlen = max(maxlen, dp1[start] + dp2[start])
	dfs_dp(0,-1)
	print(maxlen)
	```

2. 深度优先搜索：首先从任意节点 x 开始进行第一次深度优先搜索，到达距离其最远的节点，记为 y，然后再从 y 开始做第二次深度优先搜索，到达距离y 最远的节点，记为 z，则 δ(y,z) 即为树的直径，节点 y 与 节点 z 之间的距离即为直径的长度。

	```python
	# tree 是无向图的邻接表
	c = 0
	dis = [0]*4
	# 树形结构可以用父节点做参数来表示是否访问
	def dfs_e(start, f):
	    for i in tree[start]:
	        global c
	        if i == f: continue
	        dis[i] = dis[start]+1
	        if dis[i] > dis[c]: c = i
	        dfs_e(i,start)
	dfs_e(0,-1) # -1 表示一开始的父节点
	dis[c] = 0
	dfs_e(c,-1)
	print(dis[c]) # 输出树的直径
	```

## 图

迪杰斯特拉，返回从start到每个节点的最短距离

```cpp
//邻接图，包括边的长度。 g[0] = {1,4}//点0到点1的距离是4.
//返回从start到每个节点的最短距离
vector<int> djs(vector<vector<pair<int,int>>>& g, int start)
{
    vector<int> dist(g.size(), INT_MAX);
    dist[start] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.emplace(0, start);
    while(!pq.empty())
    {
        auto[d,x] = pq.top();
        pq.pop();
        if(d>dist[x]) continue; //
        for(auto[y,wt]: g[x])
        {
            int new_d = dist[x] + wt;
            if(new_d < dist[y]) //判断是否遍历过
            {
                dist[y] = new_d;
                pq.emplace(new_d, y);
            }
        }
    }
    return dist;
}

```

> 对于判断是否遍历过还是很巧妙的，对于已经遍历过的路径，已经有了dist值，如果继续添加进堆，那么其新的路径一定大于原路径，那么就无法再入堆，所以相当于已经visit过了。

## 矩阵快速幂

对于一般的快速幂，比如a的b次方，假设b的二进制是 10010100 = 148，对于每一位上a的自乘，都是指数为2次幂的，比如第三位有1，相当于a的8次方。结果就是 $a^{128}*a^{16}*a^4$， 时间复杂度变为Olog(b)。

```cpp

int fp(int a, int b)
{
	int ans = 1;
	while(b != 0)
	{
		if(b&1)
			ans *= a;
		a*=a;
		b>>1;
	}
	return ans;
}
```

接下来讲矩阵快速幂

其实矩阵快速幂，和快速幂几乎一样。优化了次方计算的量级，矩阵乘法就照算。

```cpp
typedef vector<vector<int>> mat;
mat mul(mat a, mat b)
{
	//矩阵乘法
}

int fm(mat m, int b)
{
	mat ans = E;  //单位矩阵, 未定义
	while(b != 0)
	{
		if(b&1)
			ans = mul(ans, m);
		mat = mul(mat, mat);
		b>>1;
	}
	return ans;
}
```

## 线性筛

标记哪些是质数，哪些是合数。

埃氏筛：标记2的倍数，3的倍数等，但是会有重复

欧拉筛（线性筛）：我们只用它最小的质因子去筛掉它，因此每一个数只会被筛掉一次，从而保证该筛法为线性的（效率提高到On）

```cpp
bool a[maxn];  //标记素数0，与合数1
int p[maxn],t; //记录素数数组，与素数个数
a[1]=1;//注意1不是质数；
for(int i=2; i <= n; i++)
{
	if( a[i] == 0 )
		p[++t]=i;//是质数就记录；
	for(int j=1; j<=t && i*p[j]<=n; j++)
	{
		a[ i*p[j] ]=1;//标记合数；
		if( i%p[j] == 0 )
			break;
			// p[j + 1] 一定不是 i * p[j + 1] 最小的因子了，停止继续往下筛，保证同一个合数不会被多个质数标记。
	}
}

```

> https://www.cnblogs.com/BrotherCall/p/15409308.html

## 小技巧

- int mid = left + (right - left) / 2; //二分防止计算时溢出
- vector作为参数的copy非常耗时，甚至会导致超时。所以最好传&，或者使用普通数组。
- $\frac{n}{x}$向上取整，$\frac{n+x-1}{x}$写入长度 + 对齐长度 - 1，把向上取整转换为向上取整