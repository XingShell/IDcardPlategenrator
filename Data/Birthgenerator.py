import sys
sys.path.append("..")
from idcardgenratorv2 import generator_from
if __name__ == '__main__':
    # with open('../all_personinfo','r')as f:
    #     lines = f.readlines()
    # sum = len(lines)
    # count = 0
    # import datetime
    #
    # for line in lines:
    #     count += 1
    #     if(count==10):
    #         exit()
    #     starttime = datetime.datetime.now()
    #     ename, esex, enation, eyear, emon, eday, eaddr, eidn,eorg, elife  = line.strip().split(',')
    #     generator_from(ename,esex,enation,eyear,emon,eday,eorg,elife,eaddr,eidn,isOnlyBirth=True)
    #
    #     endtime = datetime.datetime.now()
    #
    #     print(endtime - starttime)
    setBirth = set()
    for row in open("../all_personinfo"):
        ename, esex, enation, eyear, emon, eday, eaddr, eidn, eorg, elife = row.strip().split(',')
        strYMD = eyear+','+emon+','+eday
        setBirth.add(strYMD)
    print(len(setBirth)) # 88687
    for e in setBirth:
        y,m,d = e.split(',')
        generator_from(ename, esex, enation, y, m, d, eorg, elife, eaddr, eidn, isOnlyBirth=True)

