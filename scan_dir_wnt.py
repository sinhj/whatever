# -*- encoding: utf-8 -*-

# for Windows

import os
from stat import S_ISDIR, S_ISLNK



# 扫描本地 Windows host 指定目录，递归遍历目录下的文件
# 文件夹与文件不能同名
def scan_dir_wnt(wnt_dir):
    # 文件列表
    found_files = []
    # 获取本地 Windows 目录 的属性，dir /b
    dir_detl = os.listdir(wnt_dir)
    for elem in dir_detl:
        # 每一个文件或目录的路径
        _path = os.path.join(wnt_dir, elem)
        # 如果是目录，则递归处理
        if os.path.isdir(_path):
            found_files.extend(scan_dir_wnt(_path))
        else:
            found_files.append(_path)
    return found_files



# 白名单过滤指定类型
def filter_suffix(path_list, suffixs):
    aft_filter = list()
    for elem in path_list:
        for mele in suffixs:
            if elem.endswith(mele):
                aft_filter.append(elem)
    return aft_filter



# 写入 yml
def traversal(path_list, yml_path):
    for f_path in path_list:
        filename = os.path.split(f_path)[-1]
        # print f_path
        print filename



if __name__ == "__main__":
    to_scan = "D:\Doc"
    file_tree_yml = r".\txts_tree.yml"

    # traversal(scan_dir_wnt(to_scan))

    suffixs = ["ini", "jpg"]

    for elem in filter_suffix(scan_dir_wnt(to_scan), suffixs):
        print elem



    # 空文件夹补个虚文件，作为葉子节点
