import sys
sys.path.append("..")
from idcardgenratorv2 import generator_from
if __name__ == '__main__':
    setIDnumbers = set()
    for row in open("../all_personinfo"):
        ename, esex, enation, eyear, emon, eday, eaddr, eidn, eorg, elife = row.strip().split(',')
        strIDnumber = eidn
        setIDnumbers.add(strIDnumber)
    print(len(setIDnumbers)) # 2874939
    for e in setIDnumbers:
        generator_from(ename,esex,enation,eyear,emon,eday,eorg,elife,eaddr,e,isOnlyNumberID=True)