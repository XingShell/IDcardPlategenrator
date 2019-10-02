import sys
sys.path.append("..")
from idcardgenratorv2 import generator_from
if __name__ == '__main__':
    setSexgenerator = set()
    for row in open("../all_personinfo"):
        ename, esex, enation, eyear, emon, eday, eaddr, eidn, eorg, elife = row.strip().split(',')
        strSexgenerator = esex + ',' + enation
        setSexgenerator.add(strSexgenerator)
    print(len(setSexgenerator)) # 2874939
    for e in setSexgenerator:
        esex, enation = e.split(',')
        generator_from(ename,esex,enation,eyear,emon,eday,eorg,elife,eaddr,eidn,isOnlySexNation=True)