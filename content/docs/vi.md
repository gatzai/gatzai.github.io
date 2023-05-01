+++
title="Vi/Vim使用"
date=2022-11-07
in_search_index = true

categories = ["工具使用"]
tags = ["Vim","Linux"]

[extra]
toc = true
comments = false
+++

### 录制

开始录制：q + 名字

结束录制：q

播放2次：2@名字

### 替换

* 全局替换a，换成b

s/a/b/g

一个个确认是否替换，可用于间隔替换，指定替换

%s/a/b/gc

- 间隔替换
    
    搜索+录制
    

### 移动

ctrl+O    跳转到上一个位置  ， 同‘’

```bash
书签跳转
mx 设置书签，`x 跳转到书签处
这里的x可以是任意字母
```

% 跳转到括号匹配处