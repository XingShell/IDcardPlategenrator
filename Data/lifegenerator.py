import sys
sys.path.append("..")
from idcardgenratorv2 import generator_from
if __name__ == '__main__':
    setLife = set()
    for row in open("../all_personinfo"):
        ename, esex, enation, eyear, emon, eday, eaddr, eidn, eorg, elife = row.strip().split(',')
        strLife = elife
        setLife.add(strLife)
    print(len(setLife)) # 2994904
    for e in setLife:
        generator_from(ename,esex,enation,eyear,emon,eday,eorg,e,eaddr,eidn,isOnlylife=True)