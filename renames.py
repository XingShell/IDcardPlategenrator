
import os
from glob import glob

def right_replace(string, old, new, max=1):
    return string[::-1].replace(old[::-1], new[::-1], max)[::-1]
def all_replace_list(string,old,new):
    newstring = ''
    for c in string:
        index = old.find(c)
        if index != -1:
            newstring += new[index-1]
            print(c, end='--')
            print(string)
        # elif c == ' ':
        #     print(string)
        #     continue
        else:
            newstring += c
    return newstring
if __name__ == '__main__':

    dir = './Data/'
    roots = glob(os.path.join(dir,'*/*.jpg'))
    path = dir
    setPath = set()
    for filepath in roots:
        fileAllpath = path + filepath.split('/')[-2]+'/'
        setPath.add(fileAllpath)
        # print(fileAllpath)
        # exit()
        foldname = filepath.split('/')[-1]
        print(foldname)
        fnewname = all_replace_list(foldname,'（）０２１７Ｄｅ．|','()0217De.I')
        #
        # # print(fileAllpath)
        # os.rename(fileAllpath+'/'+foldname, fileAllpath+'/'+fnewname)  # 用os模块中的rename方法对文件改名


