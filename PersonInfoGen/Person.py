import numpy as np
import IDcard
class Person(object):
    NationAll = '汉族、满族、蒙古族、回族、藏族、维吾尔族、苗族、彝族、壮族、布依族、侗族、瑶族、白族、土家族、哈尼族、哈萨克族、傣族、黎族、傈僳族、佤族、畲族、高山族、拉祜族、水族、东乡族、纳西族、景颇族、柯尔克孜族、土族、达斡尔族、仫佬族、羌族、布朗族、撒拉族、毛南族、仡佬族、锡伯族、阿昌族、普米族、朝鲜族、塔吉克族、怒族、乌孜别克族、俄罗斯族、鄂温克族、德昂族、保安族、裕固族、京族、塔塔尔族、独龙族、鄂伦春族、赫哲族、门巴族、珞巴族、基诺族'
    NationAll = NationAll.split('、')
    sexAll = ['男','女']
    NationIndex = 0
    sexIndex = 0
    filename = "./lib/Chinese_Names_Corpus_Gender_120W.txt"
    filename_addr = './lib/address.txt' # 693337
    filename_gov = './lib/all_PoliceBureau'
    f = open(filename, "r").readlines()
    f = f[4:]
    findex = 0
    f_addr = open(filename_addr, "r").readlines()
    f_addr_index = 0
    f_gov = open(filename_gov, "r").readlines()
    f_gov_index = 0
    def __init__(self):
        namesex =self.__parseName_Sex()
        self.name = namesex[0]
        self.sex = namesex[1]
        # self.Nation_old = Person.NationAll[Person.NationIndex]
        self.Nation = Person.NationAll[Person.NationIndex]
        year_month_day = next(Data().get_data())
        year_month_day1 = '.'.join(map(str,next(Data().get_data())))
        year_month_day2 = '.'.join(map(str,next(Data().get_data())))

        self.year,self.month,self.day = year_month_day
        self.addr = Person.f_addr[Person.f_addr_index].strip()
        self.idcard = IDcard.IdCardGenerator().idCardGenerator()
        self.signGovment = Person.f_gov[Person.f_gov_index].strip()
        self.vaildData = year_month_day1+'-'+year_month_day2
        self.IndexAdd()
    def IndexAdd(self):
        Person.NationIndex += 1; Person.sexIndex += 1
        Person.NationIndex %= len(Person.NationAll)
        Person.sexIndex %= len(Person.sexAll)
        Person.findex += 1
        Person.findex %= len(Person.f)
        Person.f_addr_index += 1
        Person.f_addr_index %= len(Person.f_addr)
        Person.f_gov_index += 1
        Person.f_gov_index %= len(Person.f_gov)
    def output_info_p(self):
        print(self.name,end=',')
        print(self.sex,end=',')
        print(self.Nation,end=',')
        print(self.year,end=',');print(self.month,end=",");print(self.day,end=',')
        print(self.addr,end=',')
        print(self.idcard,end=',')
        print(self.signGovment,end=',')
        print(self.vaildData)
    def output_info(self,filename_all_info='./result/all_personinfo'):
        with open(filename_all_info,'a') as f:
            f.write(self.name+',')
            f.write(self.sex+',')
            f.write(self.Nation+',')
            f.write(str(self.year)+',')
            f.write(str(self.month)+",")
            f.write(str(self.day)+',')
            f.write(self.addr+',')
            f.write(self.idcard+',')
            f.write(self.signGovment+',')
            f.write(self.vaildData+'\n')
    def __parseName_Sex(self):
        return (Person.f[Person.findex].strip().split(','))

class Data(object):

    len = 10000
    year = np.random.normal(1980, 40, len)
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

# class IDcard(object):
#     idnumber = ''

if __name__ == '__main__':
    i=3000000 
    allnum = i
    # i = 20
    with open('./result/all_personinfo', 'w') as f:
        pass
    while(i):
        # print(next(Data().get_data()))
        i-=1
        Person().output_info('./result/all_personinfo')
        if i%3000==0:
            print(i/allnum)
