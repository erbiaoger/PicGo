import glob

url = '![{}](https://raw.githubusercontent.com/erbiaoger/PicGo/main/岩石标本/{})'

with open("name.txt", 'w') as f:
    for file in glob.glob('*.tiff'):
        name, _ = file.split('.')
        f.write(url.format(name, file))
        f.write('\n')
