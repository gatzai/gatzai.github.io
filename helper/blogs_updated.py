#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime
import argparse

'''
需求：
提交博客的时候自动修改更新日期

方法：
使用 python 来更新日期，并且读取文件来修改
先判断头部是否有 updated ，若没有在判断是否有date，若都没有则结束（说明这不是一个博客文档）。
'''
def update_date():
	git_root = subprocess.run(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
	os.chdir(git_root)
	print(git_root)

	updated_files = subprocess.run(['git', 'diff', '--name-only'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
	updated_file_list = (f.strip() for f in updated_files.split("\n") if f.strip().endswith(".md"))

	for updated_file_name in updated_file_list:
		#print(updated_file_name)
		with open(updated_file_name, 'r', encoding='utf-8') as f:
			content = f.read()
		temp = content.split('+++', 2)
		#判断是否符合 +++ 包围的书写规定
		if len(temp) != 3:
			print('[Warning] File: "{}" no match +++ format. Excepted {}.'.format(updated_file_name, len(temp)-1))
			continue

		frontmatter = temp[1]
		text_content = temp[2]

		#寻找两个日期的位置
		date_index = None
		updated_index = None
		items = frontmatter.split('\n')
		for (index, item) in enumerate(items):
			if item.startswith("updated"):
				updated_index = index
			if item.startswith("date"):
				date_index = index
		
		if updated_index is None:
			if date_index is None:
				#没有写日期，不是博客的形式，跳过
				print('[Info] File: "{}" is not a blog file.'.format(updated_file_name))
				continue
			else:
				print('[Info] File: "{}" updated. Added!.'.format(updated_file_name))
				items.insert(date_index+1, "updated={}".format(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")))
		else:
			print('[Info] File: "{}" updated. Updated!.'.format(updated_file_name))
			items[updated_index] = "updated={}".format(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"))
		new_frontmatter = "\n".join(items)
		new_content = "+++\n" + new_frontmatter.strip("\n") + "\n+++" + text_content
		#print(new_content)
		with open(updated_file_name, 'w', encoding='utf-8') as f:
			f.write(new_content)
# 批量替换头部字段
def replace_head():
	old_str = "updated"
	new_str = "lastmod"
	for root,dirs,files in os.walk(r"..\\content"):
		for file in files:
			#获取文件路径
			fpath = os.path.join(root,file)
			print(fpath)
			with open(fpath, 'r', encoding='utf-8') as f:
				content = f.read()
			temp = content.split('+++', 2)
			if len(temp) != 3:
				print('[Warning] File: "{}" no match +++ format. Excepted {}.'.format(fpath, len(temp)-1))
				continue

			frontmatter = temp[1]
			text_content = temp[2]
			target_index = None
			items = frontmatter.split('\n')

			# 用换行分隔，找到相应的 index 直接替换即可
			for (index, item) in enumerate(items):
				if item.startswith(old_str):
					target_index = index
					break

			if target_index is None:
				continue
			else:
				print('[Info] File: "{}" updated!.'.format(fpath))
				items[target_index] = items[target_index].replace(old_str, new_str)

			new_frontmatter = "\n".join(items)
			new_content = "+++\n" + new_frontmatter.strip("\n") + "\n+++" + text_content
			with open(fpath, 'w', encoding='utf-8') as f:
				f.write(new_content)


def run():
	replace_head()

if __name__ == "__main__":
	run()