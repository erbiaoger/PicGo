import glob
import os

url = '![{}](https://raw.githubusercontent.com/erbiaoger/PicGo/main/岩石标本/{})'

cwd = os.getcwd()
# 获取上一级目录的路径
file_dir = os.path.abspath(os.path.join(cwd, ".."))

# 获取最后一个目录名字
# dirname = os.path.basename(os.path.normpath(path))

os.chdir(os.path.join(file_dir, '岩石标本'))


with open(os.path.join(cwd, "name.txt"), 'w') as f:
    for file in glob.glob('*.png'):
        name, _ = file.split('.')
        f.write(url.format(name, file))
        f.write('\n')
