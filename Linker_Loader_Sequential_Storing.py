relocation = input("enter the relocation address of program: ")
first = input("enter first program name: ")
second = input("enter second program name: ")


def Add_relocation(sep):
    sep[1] = hex(int(sep[1], 16) + int(relocation, 16))
    sep[1] = str(sep[1])
    sep[1] = sep[1][2:]
    sep[1] = sep[1].zfill(6)
    sep[1] = sep[1].upper()
    return sep


file = open("HTE", "r")
i: int = 0
s = []
current = " "
AL = " "
BL = " "
AS = " "
BS = " "
while True:
    s.insert(i, file.readline())
    temp = s[i]
    temp = temp.split(".")
    if temp[0] == 'H':
        if temp[1] == "PROGA":
            AS = temp[2]
            AL = temp[3]
        if temp[1] == "PROGB":
            BS = temp[2]
            BL = temp[3]
    if s[i] == '':
        break
    i += 1
file.close()
i = 0
ref = []
sep = []
oc = []
x = []
m = []
for sep in s:
    sep = sep.split(".")
    t = sep[0]
    if t == "E":
        flag2 = True
    if t == "H":
        sep.pop(3)
        sep.pop(0)
        current = sep[0]
        if current == second:
            if sep[0] == "PROGA":
                relocation = hex(int(relocation,16) + int(BL, 16))
                relocation = relocation[2:]
            if sep[0] == "PROGB":
                print("f2")
                relocation = hex(int(relocation,16) + int(AL, 16))
                relocation = relocation[2:]
        relocation = str(relocation)
        relocation = relocation.zfill(6)
        sep[1] = relocation.upper()
        ref.extend(sep)
    if t == "D":
        sep.pop(0)
        while i < len(sep):
            Add_relocation(sep)
            ref.append(sep[0])
            ref.append(sep[1])
            sep.pop(0)
            sep.pop(0)
        ref.extend(sep)
        i += 2
    if t == 'M':
        sep.pop(0)
        m.extend(sep)
    if t == 'T':
        sep.pop(0)
        if current == "PROGA":
            start = hex(int(relocation, 16) + int(sep[0], 16))
        if current == "PROGB":
            start = hex(int(relocation, 16) + int(sep[0], 16))
        sep.pop(0)
        sep.pop(0)
        for x in sep:
            temp = str(start[2:])
            temp = temp.zfill(6)
            temp = temp.upper()
            oc.append(temp)
            oc.append(x)
            if len(x) == 2:
                start = hex(int(start, 16) + 1)
            if len(x) == 4:
                start = hex(int(start, 16) + 2)
            if len(x) == 6:
                start = hex(int(start, 16) + 3)
            if len(x) == 8:
                start = hex(int(start, 16) + 4)
    i += 1
print(m)
for x in m:
    address = m.pop(0)
    address = hex(int(address, 16) + int(relocation, 16))
    address = str(address)
    address = address[2:]
    address = address.zfill(6)
    address = address.upper()
    length = int(m.pop(0))
    modify = m.pop(0)
    if length == 5:
        address = hex(int(address, 16) - 1)
        temp = str(address[2:])
        temp = temp.zfill(6)
        temp = temp.upper()
        address = temp
    sign = modify[0]
    modify = modify[1:-1]
    flag = 0
    for search1 in ref:
        if search1 == modify:
            flag = 1
        if flag == 1:
            add = ref[ref.index(search1) + 1]
            break
    flag = 0
    for search2 in oc:
        if search2 == address:
            flag = 1
        if flag == 1:
            if sign == '+':
                temp = hex(int(oc[oc.index(search2) + 1], 16) + int(add, 16))
            if sign == '-':
                temp = hex(int(oc[oc.index(search2) + 1], 16) - int(add, 16))
            temp = str(temp[2:])
            temp = temp.zfill(6)
            temp = temp.upper()
            oc[oc.index(search2) + 1] = temp
            oc[oc.index(search2)]
            break
print(m)
file = open("Object Code", "w")
for i in oc:
    file.write(i)
    file.write(" ")
file.close()
file = open("External Table", "w")
i = 0
while i < len(ref) - 1:
    file.write(ref[i])
    file.write(" ")
    file.write(ref[i + 1])
    file.write("\n")
    i += 2
file.close()
