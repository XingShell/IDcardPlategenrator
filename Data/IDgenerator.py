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
    setIDnumbers = set()
    for row in open("../all_personinfo"):
        ename, esex, enation, eyear, emon, eday, eaddr, eidn, eorg, elife = row.strip().split(',')
        strIDnumber = eidn
        setIDnumbers.add(strIDnumber)
    print(len(setIDnumbers)) # 2874939
    num = 10000
    for e in setIDnumbers:
        generator_from_quick(im,ename,esex,enation,eyear,emon,eday,eorg,elife,eaddr,e,isOnlyNumberID=True)
        num -= 1
        if num <= 0:
            break
