#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from git import Repo
import time

def timestamp_to_str(timestamp, format='%b %d %H:%M:%S %Y'):
    return time.strftime(format, time.localtime(timestamp))

def str_to_timestamp(str_time, format='%Y-%m-%d %H:%M:%S'):
    return int(time.mktime(time.strptime(str_time, format)))

if __name__ == '__main__':
    # 事先准备一个本地的空Git仓库，填上路径
    repo = Repo('./1998')
    git = repo.git
    # 加载设计器导出的文件
    with open('./map.qs', 'r') as fp:
        for line in fp.readlines():
            line = line.split()
            '''
            github贡献统计时间取决于服务器位置，当前我测试发现和实际提交时间差了-16小时，
            可能是使用的旧金山的时间，我懵的，如果显示不对要自己改下后面时间。
            '''
            #os.system('date {} && time {}'.format(line[0], '16:00:00'))
            for i in range(int(line[1])):
                time_str = timestamp_to_str(str_to_timestamp(line[0] + ' 16:00:00')) + ' +0800'
                git.commit('--allow-empty', '--date=' + time_str, '-m', line[0] + '_' + str(i+1))