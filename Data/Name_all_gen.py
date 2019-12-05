import sys
sys.path.append("..")
from idcardgenratorv2 import generator_from_quick
from os.path import *
dir_path = dirname(abspath(__file__))
import PIL.Image as PImage
import os
# print('当前目录绝对路径:', dir_path)
base_dir = '../resource'
base_dir = dir_path+'/'+ base_dir
im = PImage.open(os.path.join(base_dir, 'empty.png'))
if __name__ == '__main__':
    setNames = set()
    for row in open("../all_personinfo"):
        ename, esex, enation, eyear, emon, eday, eaddr, eidn, eorg, elife = row.strip().split(',')
        strName = ename
        setNames.add(strName)
    print(len(setNames)) # 1163760
    for e in setNames:
        imcopy = im.copy()
        generator_from_quick(imcopy,e,esex,enation,eyear,emon,eday,eorg,elife,eaddr,eidn,isOnlyName=True)