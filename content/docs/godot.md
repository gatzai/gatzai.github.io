+++
title="Godot笔记"
date=2022-11-07
in_search_index = true

categories = ["工具使用"]
tags = ["Godot"]
[extra]
toc = true
comments = false
+++

# 问题

godot一些奇怪的设计：

area和shape为什么要分开设计？我觉得很奇怪，你area就不能加个shape参数吗？难道是为了要某些独立性，抑或满足不同组件的配合？反正它们都不能单独存在，配合的话也没必要这么设计。

# 项目

**相机**

获取当前相机：

**动画**

使用animationplayer节点

**移动**

**跳跃**

蹬墙跳

- is_on_wall
- raycast

跳跃

- is_on_floor

# 脚本gd

forward 怎么获取？

**坑：**

- 在层次列表，下面脚本的ready比上面脚本的ready执行顺序要后

**gdscript**

如何实例化类？Classname.new()

构造函数：func _init():

判断是否有相关属性：child.get('变量名')

三元运算：true if tri_id < 3 else false

:= 的意思

变量后面加一个冒号，自动推断类型。

也可以再加一个变量类型，用来明确变量类型，如：var a:string = “str”

RID：RID类型用于访问资源的唯一整数ID

**节点相关**

遍历子节点：self.get_children()

根节点：onready var root_node = get_node("/root/Node2D")

旋转：self.rotate() (3D)

3D位置：translation

延迟加节点：call_deferred("add_child",xxx)

实例化节点：

世界坐标转屏幕：get_global_transform_with_canvas

屏幕转世界：get_viewport().canvas_transform.affine_inverse().xform(event.position)

全局坐标：to_global(translation) 或 global_transform.origin

节点相对于父级的序号：get_index

global_transform.basis.x

**射线**

- 相机发出射线
- 物体发出射线

****Physics2DDirectSpaceState：****直接访问Physics2DServer中的空间的对象

****Transform2D: 2x3矩阵****

**鼠标**

获取鼠标屏幕位置：

屏幕到特定水平位置的世界空间？

**区域检测**

get_world_2d().direct_space_state.intersect_shape()

Geometry #二维图形相交辅助工具

**复杂遮挡**

ysort

**延时**

yield(get_tree().create_timer(.2), "timeout")  #前面代码执行完后，0.2秒后执行后面的代码

godot 重叠按钮

[https://zhuanlan.zhihu.com/p/423451617](https://zhuanlan.zhihu.com/p/423451617)

**信号**

信号添加：signal my_signal;

信号绑定：connect(”my_signal”, self, “_signal_func”);

信号触发：emit_signal(”my_signal”);

# 项目导出

**导出到HTML5**

由于安全问题，浏览器不支持file://格式的资源加载。

所以运行这玩意需要在服务器上。

(貌似主界面的右上角有html5的按钮）

# 模型和动画导入

从blender导入模型和动画注意

- 导出glTF2.0
- 格式设置为glTF嵌入式(.gltf)
- 其他自行设置（注意骨骼）

在godot里面的动画和模型都是灰色的，表示无法改动。

所以需要右键场景，选择清除继承。

导出多个动画还需要：选择每个动画片段的NLA

> [https://www.youtube.com/watch?v=FW8w6X1fLg8](https://www.youtube.com/watch?v=FW8w6X1fLg8)
> 

# 渲染

**Shader**

在片段着色器里面获取模型坐标，很迷的操作，在项目里面有。

**材质**

如何批量修改？

**光照**

环境光和直射光的调节

[https://www.youtube.com/watch?v=8kwnCxK8Vc8](https://www.youtube.com/watch?v=8kwnCxK8Vc8)

# 插件与辅助

麻烦的一批

> [https://www.youtube.com/watch?v=qxQxzNpPXDU](https://www.youtube.com/watch?v=qxQxzNpPXDU)
> 

获取场景

get_tree().get_edited_scene_root()

好了，这个材质替换的插件可以不用做了。有别的方法：

1. 把原来的材质改了（删了也行，只要名字相同就可以）
2. 重新覆盖原场景
3. 重启godot

Gizmo：

> [https://randommomentania.com/2019/01/godot-runtime-3d-gizmo-tutorial-part-1/](https://randommomentania.com/2019/01/godot-runtime-3d-gizmo-tutorial-part-1/)
> 

**EditorInspectorPlugin**

can_handle  #当你在场景树选中某个条目时，这个会判断，便于对特定类型判断

parse_begin #inspector头部

parse_end #inspector尾部

parse_catergory #inspector子类头部

# UI

**按钮**

用代码控制按钮事件
```python
func _enter_tree():
        connect("pressed",self,"_on_btn_click")
func _exit_tree():
        disconnect("pressed",self,"_on_btn_click")
func _on_btn_click():
        print("do something...")
```