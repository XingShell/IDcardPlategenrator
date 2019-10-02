# coding:utf-8
import os
import PIL.Image as PImage
from PIL import ImageFont, ImageDraw
import cv2
import numpy as np




def changeBackground(img, img_back, zoom_size, center):
    # 缩放
    img = cv2.resize(img, zoom_size)
    rows, cols, channels = img.shape

    # 转换hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 获取mask
    #lower_blue = np.array([78, 43, 46])
    #upper_blue = np.array([110, 255, 255])
    diff = [5, 30, 30]
    gb = hsv[0, 0]
    lower_blue = np.array(gb - diff)
    upper_blue = np.array(gb + diff)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # cv2.imshow('Mask', mask)

    # 腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)
    dilate = cv2.dilate(erode, None, iterations=1)

    # 粘贴
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 0:  # 0代表黑色的点
                img_back[center[0] + i, center[1] + j] = img[i, j]  # 此处替换颜色，为BGR通道

    return img_back

def paste(avatar, bg, zoom_size, center):
    avatar = cv2.resize(avatar, zoom_size)
    rows, cols, channels = avatar.shape
    for i in range(rows):
        for j in range(cols):
            bg[center[0] + i, center[1] + j] = avatar[i, j]
    return bg
from os.path import *
#     im.save('color.png')
#     im.convert('L').save('bw.png')
#
#     showinfo(u'成功', u'文件已生成到目录下,黑白bw.png和彩色color.png')
def generator_from(ename,esex,enation,eyear,emon,eday,eorg,elife,eaddr,eidn,\
                   isOnlyAddr=False,isOnlyName=False,isOnlySexNation=False,isOnlyBirth=False,\
                   isOnlyNumberID=False, isOnlyGovSige=False, isOnlyLife=False):
    name = ename
    sex = esex
    nation = enation
    year = eyear
    mon = emon
    day = eday
    org = eorg
    life = elife
    addr = eaddr
    idn = eidn

    dir_path = dirname(abspath(__file__))
    # print('当前目录绝对路径:', dir_path)
    base_dir = './resource'
    base_dir = dir_path+'/'+ base_dir
    im = PImage.open(os.path.join(base_dir, 'empty.png'))
    # avatar = PImage.open(fname)  # 500x670

    name_font = ImageFont.truetype(os.path.join(base_dir, 'hei.ttf'), 72)
    other_font = ImageFont.truetype(os.path.join(base_dir, 'hei.ttf'), 60)
    bdate_font = ImageFont.truetype(os.path.join(base_dir, 'fzhei.ttf'), 60)
    id_font = ImageFont.truetype(os.path.join(base_dir, 'ocrb10bt.ttf'), 72)

    namebox = (430, 690, 900, 780)
    sexnationBox = (430, 840, 1200, 900)
    birthbox = (430, 950, 1300, 1050)
    addrbox = (430, 1090, 1400, 1220)
    idnbox = (430, 1450, 1800, 1550)
    signGovbox = (700, 2750, 1800, 2840)
    lifebox = (700, 2860, 1800, 2990)

    Box = (namebox, sexnationBox, birthbox, addrbox, idnbox, signGovbox, lifebox)
    Info = ('姓名' + name,\
            '性别' + sex + '民族' + nation, \
            '出生' + year + '年' + mon + '月' + day + '日', \
            '住址' + addr, \
            '身份号码' + idn, \
            '签发机关' + org, \
            '有效期限' + life
            )

    draw = ImageDraw.Draw(im)
    index = -1
    if True not in ( isOnlyAddr,isOnlyName,isOnlySexNation,isOnlyBirth,isOnlyNumberID, isOnlyGovSige, isOnlyLife):
        draw.text((630, 690), name, fill=(0, 0, 0), font=name_font)
        draw.text((630, 840), sex, fill=(0, 0, 0), font=other_font)
        draw.text((1030, 840), nation, fill=(0, 0, 0), font=other_font)
        draw.text((630, 980), year, fill=(0, 0, 0), font=bdate_font)
        draw.text((950, 980), mon, fill=(0, 0, 0), font=bdate_font)
        draw.text((1150, 980), day, fill=(0, 0, 0), font=bdate_font)
        start = 0
        loc = 1120
        while start + 11 < len(addr):
            draw.text((630, loc), addr[start:start + 11], fill=(0, 0, 0), font=other_font)
            start += 11
            loc += 100
        draw.text((630, loc), addr[start:], fill=(0, 0, 0), font=other_font)
        draw.text((950, 1475), idn, fill=(0, 0, 0), font=id_font)
        draw.text((1050, 2750), org, fill=(0, 0, 0), font=other_font)
        draw.text((1050, 2895), life, fill=(0, 0, 0), font=other_font)

        for i in range(7):
            box = Box[i]
            info = Info[i]
            save_plate(info,box,im)
    else:
        if isOnlyName:
            draw.text((630, 690), name, fill=(0, 0, 0), font=name_font)
            index = 0
        if isOnlySexNation:
            draw.text((630, 840), sex, fill=(0, 0, 0), font=other_font)
            draw.text((1030, 840), nation, fill=(0, 0, 0), font=other_font)
            index = 1
        if isOnlyBirth:
            draw.text((630, 980), year, fill=(0, 0, 0), font=bdate_font)
            draw.text((950, 980), mon, fill=(0, 0, 0), font=bdate_font)
            draw.text((1150, 980), day, fill=(0, 0, 0), font=bdate_font)
            index = 2
        if isOnlyAddr:
            start = 0
            loc = 1120
            while start + 11 < len(addr):
                draw.text((630, loc), addr[start:start + 11], fill=(0, 0, 0), font=other_font)
                start += 11
                loc += 100
            draw.text((630, loc), addr[start:], fill=(0, 0, 0), font=other_font)
            index = 3
        if isOnlyNumberID:
            draw.text((950, 1475), idn, fill=(0, 0, 0), font=id_font)
            index = 4
        if isOnlyGovSige:
            draw.text((1050, 2750), org, fill=(0, 0, 0), font=other_font)
            index = 5
        if isOnlyLife:
            draw.text((1050, 2895), life, fill=(0, 0, 0), font=other_font)
            index = 6
        save_plate(Info[index], Box[index], im)


def save_plate(savedir, box, im):
    box = list(box)

    Dir = None
    if savedir[0:2]!='住址':
        a = im.crop(box).convert('RGB')
        if savedir[0:2]=='姓名':
            Dir = 'Name/'
        elif savedir[0:2]=='性别':
            Dir = 'Sex/'
        elif savedir[0:2]=='出生':
            Dir = 'Birth/'
        elif savedir[0:2] == '身份':
            Dir = 'ID/'
        elif savedir[0:4] == '签发机关':
            Dir = 'Sign/'
        elif savedir[0:4] == '有效期限':
            Dir = 'life/'
        else:
            return -1
        dir_path = dirname(abspath(__file__))
        base_dir = './Data/'
        base_dir = dir_path + '/' + base_dir
        a.save(base_dir+Dir+savedir+'.jpg')
    else:
        Dir = 'Addr/'
        dir_path = dirname(abspath(__file__))
        base_dir = './Data/'
        base_dir = dir_path + '/' + base_dir
        start = 2
        loc = 1120
        if start + 11 < len(savedir):
            a = im.crop(box).convert('RGB')
            a.save(base_dir+Dir+savedir[0:start+11]+'.jpg')
            start += 11
        box[0] = 610
        box[1] += 100
        box[3] += 100
        while start + 11 < len(savedir):
            a = im.crop(box).convert('RGB')
            a.save(base_dir + Dir + savedir[start:] + '.jpg')
            start += 11
            box[1] += 100
            box[3] += 100
        if start < len(savedir):
            a = im.crop(box).convert('RGB')
            a.save(base_dir + Dir + savedir[start:] + '.jpg')




if __name__ == '__main__':
    with open('./all_personinfo','r')as f:
        lines = f.readlines()
    sum = len(lines)
    import datetime

    for line in lines:
        starttime = datetime.datetime.now()
        ename, esex, enation, eyear, emon, eday, eaddr, eidn,eorg, elife  = line.strip().split(',')
        generator_from(ename,esex,enation,eyear,emon,eday,eorg,elife,eaddr,eidn)

        endtime = datetime.datetime.now()

        print(endtime - starttime)
        exit()


