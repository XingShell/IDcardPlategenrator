# coding = utf-8
import json
import re
from random import randint
def loadAddr():
    f = open("address.json", encoding='utf-8')  
    contents = json.load(f)
    return contents

t = loadAddr()

special_province = {
    "内蒙古自治区": "内蒙古",
    "广西壮族自治区": "广西",
    "西藏自治区": "西藏",
    "宁夏回族自治区": "宁夏",
    "新疆维吾尔自治区": "新疆",
}
def prosseVillage(village):
    address = ''
    if re.search(r'(村|里|屯|湾|田)$', village):
        address += village
        a = randint(1, 20)
        b = randint(1, 100)
        if a > 10:
            address += "{0}组{1}号".format(a, b)
        else:
            address += "{0}号".format(b)
    elif re.search(r'路', village):
        a = randint(1, 500)
        index = village.find('路')
        address += village[: index + 1] + "{0}号".format(a)
    elif re.search(r'街', village):
        a = randint(1, 500)
        index = village.find('街')
        address += village[: index + 1] + "{0}号".format(a)
    elif re.search(r'社区', village):
        village = re.sub(r'社区', '', village)
        a = randint(1, 20)
        b = randint(1, 6)
        c = randint(1, 10)
        d = randint(1, 4)
        address += village + "{0}幢{1}单元{2}0{3}".format(a, b, c, d)
    else:
        address += village
    return address
    
def generate_address(filesoure,special_province=special_province):
    five_addr = []
    for province,SecondAddr in filesoure.items():  
        for city, ThreeAddr in SecondAddr.items():
            if re.search(r'市$', province):
            # 天津市 市辖区 
                city = ''
            if re.search(r'自治区$', province):
                province = special_province[province]
                if re.search(r'直辖', city):
                    city = ''
                else:
                    pass
                # print(province+city)
            
            # 乡，镇
            for county,FouthAddr in ThreeAddr.items():
                for town,FifthAddr in FouthAddr.items():
                    if re.search(r'街道办事处$', town):
                        town = town[:-4]
                    elif  re.search(r'地区办事处$', town):
                    #街道办事处作为县级政府的派出机构，不是一级政府，不能作为户籍地址的标准名称
                        town = ''
                    elif re.search(r'办事处$', town):
                        town = town[:-3]
                    else:
                        pass
                    for village in FifthAddr:
                        five_addr.append(province+city+county+town+prosseVillage(village))
    return five_addr
                    
                   
                    

AddrPre = generate_address(t)
with open('newaddAddr.txt','w',encoding='utf-8')as f_writer:
    for line in AddrPre:
        f_writer.writelines(line+'\n')
    
                
                