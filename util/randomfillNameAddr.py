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

def generator_from_quick(im,string):
    name_font = ImageFont.truetype(os.path.join(base_dir, 'hei.ttf'), 72)
    other_font = ImageFont.truetype(os.path.join(base_dir, 'hei.ttf'), 60)
    bdate_font = ImageFont.truetype(os.path.join(base_dir, 'fzhei.ttf'), 60)
    id_font = ImageFont.truetype(os.path.join(base_dir, 'ocrb10bt.ttf'), 72)

    draw = ImageDraw.Draw(im)
    start = 0
    loc = 1120
    while start + 11 < len(string):
        draw.text((630, loc), string[start:start + 11], fill=(0, 0, 0), font=other_font)
        start += 11
        loc += 100
    draw.text((630, loc), string[start:], fill=(0, 0, 0), font=other_font)


    box = (610,1100,1400,1190)
    save_plate(string,box,im)


def save_plate(string, box, im):
    Dir = 'Random/'
    start = 0
    loc = 1120
    box =list(box)
    while start + 11 < len(string):
        a = im.crop(box).convert('RGB')
        a.save('./Data/' + Dir + string[start:start + 11]+'.jpg')
        start += 11
        box[1] += 100
        box[3] += 100
    if start < len(string):
        a = im.crop(box).convert('RGB')
        a.save('./Data/' + Dir + string[start:] + '.jpg')




if __name__ == '__main__':
    from allPosibleChars import AllPossibleChinese as strings
    from allPosibleChars import loadstring
    s = loadstring(3,10,2000)
    # strings = '12345678901ewqdqwdwqe13212e12e211d43r34gvreg390jg9035j4g90j49gj903j90gj390gj30gj'
    i = 0
    base_dir = './resource'
    im = PImage.open(os.path.join(base_dir, 'empty.png'))

    for chars in s:
        i += 1
        if i%500 == 0:
            print('have %d',len(s)-i)
        img = im.copy()
        generator_from_quick(img,chars)
