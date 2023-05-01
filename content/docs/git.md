+++
title="Git使用"
date=2022-11-10
lastmod=2023-03-01T10:50:59.000Z
in_search_index = true
editURL = "https://github.com/silentbluedrop/"
latex = true

categories = ["工具使用"]
tags = ["git","版本控制"]
[extra]
toc = true
comments = false
+++

git使用笔记

<!--more-->

流程图

{{< mermaid >}}
flowchart LR
repo[(Repository)]
rmo[(Remote)]
id[(index)]
work>工作目录] 
style work fill:#FE4A49;

subgraph local
repo
id
work
end

rmo --fetch/clone--> repo[(Repository)]
rmo --pull---> work

work --add--> id
repo --checkout--> work
repo --push--> rmo
id --commit--> repo
{{< /mermaid >}}


## 基础

### 用户
```git
    //全局用户
    // 查看如下，若要修改则直接在后面加内容，也可以在配置文件 config 内修改
    git config --global user.name
    git config --global user.email
    //局部（仓库）用户
    // 也可以加上关键字 --local
    git config user.name
    git config user.email
```

### 添加
```git
#添加所有：
git add .

#或者：
git add --all

#撤回添加：
git reset
```

### 查看修改历史

```git
# 查看 README.md 文件最近三次的修改
git show -3 README.md

# 直接查看某次修改
git show <sha>
```

### reset 和 checkout 和 revert

* reset 是强制调到某个版本
    1. log会变化，reset到origin之前的位置会导致origin之后的提交不见，可以通过reflog查询相关的提交号
    2. 文件内容不变

* checkout 是将文件还原到当前版本
    1. log不会变化
    2. 文件内容变化，变回当前的版本

* git revert是用一次新的commit来回滚之前的commit，此次提交之前的commit都会被保留
    1. log？
    2. 文件？

### 还原文件

对于未暂存的：git checkout “filename”


### 把文件恢复到某个commit

先查看版本号git log

然后git reset 版本号

### 已经 push 了，回滚到之前的版本

```git
git reset --hard 回退到的版本号
git push -f origin 分支名字
```

```
# 一些快速回退
git reset --hard HEAD^ #回退到上次
git reset --hard HEAD~2 #回退到上两次
```

### 取消跟踪

git rm --cached <文件名>   //取消跟踪，但不删除文件

git rm --f <文件名>   //取消跟踪，且不删除文件

（如果是文件夹则加-r）

### 撤销提交

```git
# HEAD^的意思是上一个版本，也可以写成HEAD~1
git reset --soft HEAD^

# 如果你进行了2次commit，想都撤回，可以使用HEAD~2
git reset --soft HEAD~2 #回退到上两次
```

这个命令相当于删除提交记录，但是不修改文件内容。

### “撤销’撤销提交‘”

使用git reflog 来查看HEAD的历史。

用git reset --hard "SHA"恢复到特定时期的项目。

⚠️注意：上面这个命令会将没有跟踪的，以及commit的文件清空，谨慎使用。

真正的撤销‘撤销提交’，把上面的--hard 改为 --soft，然后看清"SHA"就行了。

## 分支

### 拉取远程分支（本地没有）

git fetch

git checkout -b 本地分支名 origin/远程分支名 

### 合并分支（dev合并到master）

git checkout master

git merge dev

git push origin master    //推送至远程master

查看所有分支：git branch -a      //这个更新不及时，应该是缓存，用git fetch origin --prune。

分支切换：git checkout 分支名

查看本地和远程分支的关联：git branch -vv

删除本地dev分支：git branch -d dev

删除远程dev分支：git push origin -d dev

问题：某个分支已经合并到主分支了并且提交了，但是主机B的本地还有两个分支。如何保证主机B的分支与远程同步？

答：直接删掉远程的分支即可。

## 子模块

### submodule

* 添加子模块：

git submodule add <子模块git项目地址> <路径>

(如果有报错存在index，请确保路径的目录是一个新目录)

* 手动更新子模块

有时候子模块过大，不想用命令 `git submodule add`，能否手动添加相应的配置文件呢？

答案是不可能的，参考如下。简单来说就是`.git/index`内容会有变化，无法手动维护。

> https://stackoverflow.com/questions/24777973/adding-git-submodules-automatically-gitmodules

* 子模块更新：
```git

git submodule update --remote

git add <被更新的文件>

git commit ..

git push
```

* 删除子模块

1. 先删除子模块的目录: `git rm --cached 子模块名称`
2. 移除 `.gitmodules` 子模块对应的信息
3. 移除 `.git/modules` 中对应的信息
4. 移除 `.git/config` 中对应的信息
5. 添加修改并提交

* 面对多个提交找bug

git bitsect

修改submodule是否能提交，并且不修改源项目？

从原理上来说是不可能的，而且也比较傻逼

SourceTree参考：

[https://blog.csdn.net/lgxzzz/article/details/122884557](https://blog.csdn.net/lgxzzz/article/details/122884557)


## 情景

今天呢，我commit一个文件夹（我以为commit了，但其时没commit，因为里面有几个文件忘了放.gitignore了），当前状态A，然后我撤销提交，当前状态A-1。

然后呢，我看错了，以为没成功，然后又撤销了一遍，当前状态A-2。（可以救，但不好救）

（从现在开始，没救了）然后反悔了，直接恢复到特定时期的提交，恢复到A-1，然后我A状态新增的文件全部没了。所以要小心啊！

## 代理

github访问太慢了，需要代理

### 添加http代理

git config --global http.proxy "http://127.0.0.1:8001"

git config --global https.proxy "http://127.0.0.1:8001"

这里的代理地址可以使用v2ray配置的地址的端口

### 取消设置

git config --global --unset http.proxy

git config --global --unset https.proxy

> [https://www.cnblogs.com/runnerjack/p/9342362.html](https://www.cnblogs.com/runnerjack/p/9342362.html)
