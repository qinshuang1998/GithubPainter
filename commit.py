# code reference https://github.com/qinshuang1998/GithubPainter
from git import Repo
import time
from tqdm import tqdm
import argparse
import os

def timestamp_to_str(timestamp, format='%b %d %H:%M:%S %Y'):
    return time.strftime(format, time.localtime(timestamp))

def str_to_timestamp(str_time, format='%Y-%m-%d %H:%M:%S'):
    return int(time.mktime(time.strptime(str_time, format)))

if __name__ == '__main__':
    # -------------ArgumentParser Object----------------#
    parser = argparse.ArgumentParser()  
    parser.add_argument('-i', type=str, help="local path of git repo")
    args = parser.parse_args()
    # -------------ArgumentParser Object----------------#
    if args.i:
        print("commit to", args.i)
        repo = Repo(args.i)
        git = repo.git
        # 加载设计器导出的文件
        with open('./map.qs', 'r') as fp:
            for line in tqdm(fp.readlines()):
                line = line.split()
                '''
                github贡献统计时间取决于服务器位置，当前我测试发现和实际提交时间差了-16小时，
                可能是使用的旧金山的时间，我懵的，如果显示不对要自己改下后面时间。
                '''
                #os.system('date {} && time {}'.format(line[0], '16:00:00'))
                for i in range(int(line[1])):
                    time_str = timestamp_to_str(str_to_timestamp(line[0] + ' 16:00:00')) + ' +0800'
                    git.commit('--allow-empty', '--date=' + time_str, '-m', line[0] + '_' + str(i+1))
    else:
        print("Please input your repo path!")
        print(os.system("python .\commit.py -h"))
