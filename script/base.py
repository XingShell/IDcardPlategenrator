import sys,os
import numpy as np
sys.path.append("../lib")
from idcardgenratorv2 import generator_from_quick
import argparse
from os.path import *
from tqdm import tqdm

import PIL.Image as PImage
base_dir = os.path.join(dirname(abspath(__file__)),'../resource')
im = PImage.open(os.path.join(base_dir, 'empty.png'))


parser = argparse.ArgumentParser()
parser.add_argument('--filepath',type=str,help='信息来源相对路径',default='.')
parser.add_argument('--model',type=int,help='名字:1 '
'身份证号码:2 '
'生日:3 '
'性别民族:4 '
'地址:5 '
'签发机关:6 '
'验证日期:7')
parser.add_argument('--numbers',type=int,help='身份证号码数量',default=100)

opt = parser.parse_args()
class Data(object):
    len = 100000
    year = np.random.normal(1980, 60, len)
    year = year.astype(int)
    index = 0
    def get_data(self):
        Data.index += 1
        Data.index %= Data.len
        month = np.random.randint(1,13)
        if month == 2:
            if Data.year[Data.index]%400==0 or\
                (Data.year[Data.index]%4==0 and Data.year[Data.index]%100!=0):
                day = np.random.randint(1,30)
            else:
                day = np.random.randint(1,29)
        elif month in [1,3,5,7,8,10,12]:
            day = np.random.randint(1,32)
        else:
            day =np.random.randint(1,31)
        yield Data.year[Data.index],month,day
def getIndex(model):
    # isOnlyAddr=False,isOnlyName=False,isOnlySexNation=False,isOnlyBirth=False,isOnlyNumberID=False, isOnlyGovSige=False, isOnlyLife=False
    # ename,esex,enation,eyear,emon,eday,eorg,elife,eaddr,eidn
    if model == 1:
        # 名字
        # Chinese_Names_Corpus_Gender（120W）.txt
        indexBool = 1 ; indexStringInfo = [0]
    elif model == 2:
        # 身份证号码
        indexBool = 4 ; indexStringInfo = [9]
    elif model == 3:
        # 生日
        indexBool = 3 ; indexStringInfo = [3,4,5]
    elif model == 4:
        # 性别民族
        # 民族.txt
        indexBool = 2 ; indexStringInfo = [1,2]
    elif model == 5:
        # 地址
        # newaddAddr.txt
        indexBool = 0 ; indexStringInfo = [8]
    elif model == 6:
        # 签发机关
        # 签发机关v1.txt
        indexBool = 5 ; indexStringInfo = [6]
    else:
        # 验证日期
        indexBool = 6 ; indexStringInfo = [7]
    return indexBool,indexStringInfo


# from collections import Iterable

def readFileTool(filepath, infoset,model,numbers=0):
    if model == 5 or model == 6:
        for row in open(filepath,'r',encoding='utf-8'):
            tem = row.strip()
            if len(tem)>0:
                infoset.add(tem)
    elif model == 1:
        lastName = set()
        firstName = set()
        with open(filepath,'r',encoding='utf-8') as f:
            f.readline();f.readline();f.readline();f.readline()
            for name in f.readlines():
                if len(name.strip())==0:
                    pass
                else:
                    name = name.strip().split(',')[0]
                    lastName.add(name[1:])
                    firstName.add(name[0])
        lastName = list(lastName) #133134
        firstName = list(firstName) # 734
        for index in range(len(lastName)):
            infoset.add(firstName[index%len(firstName)]+lastName[index])
    elif model == 2:
        import IDcard
        for n in range(numbers):
            idnumber = IDcard.IdCardGenerator().idCardGenerator()
            infoset.add(idnumber)        
    elif model == 4:
        infoset = list(infoset)
        with open(filepath,'r',encoding='utf-8') as f:
            nations = f.readline().split('、')  
        for gender in ['男','女']:
            for n in nations:
                infoset.append([gender,n])
    elif model == 3:
        infoset = list(infoset)
        for n in range(numbers):
            year_month_day = next(Data().get_data())
            year,month,day = year_month_day
            infoset.append([str(year),str(month),str(day)])
    elif model == 7:
        for n in range(numbers):
            year_month_day1 = '.'.join(map(str,next(Data().get_data())))
            year_month_day2 = '.'.join(map(str,next(Data().get_data())))
            vaildData = year_month_day1+'-'+year_month_day2
            infoset.add(vaildData)
    return infoset

def readNameAll(filepath, infoset,model):
    if model == 1:
        with open(filepath,'r',encoding='utf-8') as f:
            f.readline();f.readline();f.readline();f.readline()
            for name in f.readlines():
                if len(name.strip())==0:
                    pass
                else:
                    name = name.strip().split(',')[0]
                    infoset.add(name)
    


def genfun():
    
    infoset= set()
    filepath = os.path.join(dirname(abspath(__file__)),opt.filepath)
    model = opt.model

    infoset = readFileTool(filepath,infoset,model,opt.numbers)

    
    ename,esex,enation,eyear,emon,eday,eorg,elife,eaddr,eidn = range(10)
    InputargStr = ['0123456']*10
    InputargBool = [False]*7
    indexBool = ''; indexStringInfo = ''


    indexBool, indexStringInfo = getIndex(model)
    InputargBool[indexBool] = True
    for e in tqdm(infoset):
        imcopy = im.copy()
        if isinstance(e,list):
            for i,j in enumerate(indexStringInfo):
                InputargStr[j] = e[i]
        else:
            InputargStr[indexStringInfo[0]] = e
        
        generator_from_quick(imcopy,*InputargStr,*InputargBool)
    
        
        

if __name__ == '__main__':
    genfun()