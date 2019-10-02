import sys
sys.path.append("..")
from idcardgenratorv2 import generator_from
if __name__ == '__main__':
    setNames = set()
    for row in open("../all_personinfo"):
        ename, esex, enation, eyear, emon, eday, eaddr, eidn, eorg, elife = row.strip().split(',')
        strName = ename
        setNames.add(strName)
    print(len(setNames)) # 1163760
    for e in setNames:
        generator_from(e,esex,enation,eyear,emon,eday,eorg,elife,eaddr,eidn,isOnlyName=True)