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
    # setNames = list(setNames)
    lastName = set()
    firstName = set()
    for e in setNames:
        lastName.add(e[0])
        firstName.add(e[1:])
    N = (len(lastName)) # 734
    print(len(firstName)) # 133134
    firstName = list(firstName)
    lastName = list(lastName)
    simplyName = []
    for index in range(len(firstName)):
        Name = lastName[index%N]+firstName[index]
        # print(Name)
        simplyName.append(Name)

    print(len(simplyName))
    setNames = simplyName
    for e in setNames:
        generator_from(e,esex,enation,eyear,emon,eday,eorg,elife,eaddr,eidn,isOnlyName=True)