#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from git import Repo
import os

if __name__ == '__main__':
    repo = Repo('./1998')
    git = repo.git
    '''
    can use below, waiting for my update...
    git.commit('--allow-empty', '--date="月 日 时间 年 +0800"', '-m', '')
    '''
    with open('./map.qs', 'r') as fp:
        for line in fp.readlines():
            line = line.split()
            '''
            UTC时区加上浏览时js判断的时区，会导致实际差了16小时，我懵的
            '''
            os.system('date {} && time {}'.format(line[0], '16:00:00'))
            for i in range(int(line[1])):
                git.commit('--allow-empty', '-m', line[0] + '_' + str(i+1))