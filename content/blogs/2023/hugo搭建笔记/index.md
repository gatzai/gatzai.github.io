+++
title="Hugo 博客搭建笔记"

date=2023-05-02

tags = ["博客"]

+++

从 Zola 转向 Hugo 小记

<!--more-->

## 从 Zola 到 Hugo

`Zola` 无疑非常简洁和优雅，这既是她的优点也是缺点。对于专注博客内容的人可能会很喜欢，但对于我来说还是有些单调。
从 `Zola` 转到 `Hugo` 主要是因为看到了非常棒的主题 `blowfish`。
其实 `Hugo` 的文件结构与 `Zola` 几乎是同一种类型，熟悉了 `Zola` 就很容易转移到 `Hugo` 了。 

`_index.md` 文件，将当前文件目录分成一个单独的博客页面入口。不要使用 `index.md` 命名，这会使整个博客的文章消失或者混乱。

## blowfish 主题

本博客使用了 blowfish 主题，选择这个主题的原因：

* 好看，模糊材质的质感加上非常优雅的白天黑夜模式
* 文档齐全，花一天时间照着文档做，基本就能摸透所有功能
* 支持多语言，甚至还有RTL模式（从右到左阅读）
* 完整的中英文搜索功能

使用下来，还是发现了一点小缺点：

* 部分页面卡顿，比如标签页面。如果文章变多了，可能会是一个隐患。

## Hugo + Github Page + Github Action

这篇教程[1]的部署方式不太优雅，它需要把构建出来的 build 文件发布到 master 分支上，虽然问题不大，但是看着不爽。
而之前 `Zola` 部署方式甚是优雅，完全无痕。我就想能否保持 hugo 的构建方式，将部署方式改成 zola的，结果很完美。

Github Action 分两个部分，分别是在 job 里面的 build 和 deploy。脚本如下：
```yaml
name: Deploy website to Pages

on:
    push:
    workflow_dispatch:
    schedule:
        # Runs everyday at 8:00 AM
        - cron: "0 0 * * *"

# 设置权限，Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
    contents: read
    pages: write
    id-token: write

jobs:
    # hugo 构建
    build:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout
              uses: actions/checkout@v2
              with:
                  submodules: true
                  fetch-depth: 0

            - name: Setup Hugo
              uses: peaceiris/actions-hugo@v2
              with:
                  hugo-version: "latest"

            - name: Build Web
              run: hugo

            - name: Upload artifact
              uses: actions/upload-pages-artifact@v1
              with:
                path: ./public

    # hugo 部署，参考 Zola 的部署方式
    deploy:
      environment:
        name: github-pages
        url: ${{ steps.deployment.outputs.page_url }}
      runs-on: ubuntu-latest
      needs: build
      steps:
        - name: Deploy to GitHub Pages
          id: deployment
          uses: actions/deploy-pages@v1
```

> 1. [搭建你的博客自动发布系统](https://sspai.com/post/73512)