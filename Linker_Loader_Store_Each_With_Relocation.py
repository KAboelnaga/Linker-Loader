RA = input("enter the relocation address of PROGA: ")
RB = input("enter the relocation address of PROGB: ")

def Add_relocation(sep):
    if current == "PROGA":
        sep[1] = hex(int(sep[1], 16) + int(RA, 16))
    if current == "PROGB":
        sep[1] = hex(int(sep[1], 16) + int(RB, 16))
    sep[1] = str(sep[1])
    sep[1] = sep[1][2:]
    sep[1] = sep[1].zfill(6)
    sep[1] = sep[1].upper()
    return sep
file = open("HTE", "r")
i: int = 0
s = []
current = " "
while True:
    s.insert(i, file.readline())
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
    if t == "H":
        sep.pop(0)
        current = sep[0]
        if sep[0] == "PROGA":
            sep[1] = RA
            RAL = sep.pop(2)
        if sep[0] == "PROGB":
            sep[1] = RB
            RBL = sep.pop(2)
        sep[1] = str(sep[1])
        sep[1] = sep[1].zfill(6)
        sep[1] = sep[1].upper()
        ref.extend(sep)
    if t == "D":
        sep.pop(0)
        i = 0
        while i <= len(sep):
            if current == "PROGA":
                sep[1] = hex(int(sep[1], 16) + int(RA, 16))
            if current == "PROGB":
                sep[1] = hex(int(sep[1], 16) + int(RB, 16))
            sep[1] = str(sep[1])
            sep[1] = sep[1][2:]
            sep[1] = sep[1].zfill(6)
            sep[1] = sep[1].upper()
            ref.append(sep.pop(0))
            ref.append(sep.pop(0))
            i += 2
    if t == 'M':
        sep.pop(0)
        address = sep.pop(0)
        if current == "PROGA":
            address = hex(int(RA, 16) + int(address, 16))
        if current == "PROGB":
            address = hex(int(RB, 16) + int(address, 16))
        address = str(address)
        address = address[2:]
        address = address.zfill(6)
        address = address.upper()
        sep.insert(0, address)
        m.extend(sep)
    if t == 'E':
        oc.append("\n")
    if t == 'T':
        sep.pop(0)
        if current == "PROGA":
            start = hex(int(RA, 16) + int(sep[0], 16))
        if current == "PROGB":
            start = hex(int(RB, 16) + int(sep[0], 16))
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
file = open("Modifications", "w")
for i in m:
    file.write(i)
    file.write(" ")
file.close()
count = 0
i = 0
while i < len(m):
    address = m.pop(0)
    length = int(m.pop(0))
    modify = m.pop(0)
    if length == 5:
        address = hex(int(address, 16) - 1)
        address = str(address[2:])
        address = address.zfill(6)
        address = address.upper()
    sign = modify[0]
    modify = modify[1:-1]
    flag = 0
    for search1 in ref:
#        if search1
        if search1 == modify:
            flag = 1
            add = ref[ref.index(search1) + 1]
            if add[len(add)-1] == '\n':
                add = add[:-2]
            flag = 0
            for search2 in oc:
                if search2 == address:
                    flag = 1
                    if oc[oc.index(search2) + 1][-1] == '\n':
                        oc[oc.index(search2) + 1] = oc[oc.index(search2) + 1][:-1]
                    if sign == '+':
                        modi = hex(int(oc[oc.index(search2) + 1], 16) + int(add, 16))
                    if sign == '-':
                        modi = hex(int(oc[oc.index(search2) + 1], 16) - int(add, 16))
                    if flag == 1:
                        modi = str(modi)
                        modi = modi[2:]
                        modi = modi.zfill(6)
                        modi = modi.upper()
                        oc[oc.index(search2) + 1] = modi
                        count += 1
                        break

file = open("Object Code 2", "w")
for i in oc:
    file.write(i)
    file.write(" ")
file.close()
file = open("External Table 2", "w")
i = 0
while i < len(ref) - 1:
    file.write(ref[i])
    file.write(" ")
    file.write(ref[i + 1])
    file.write("\n")
    i += 2
file.close()
i = 0
ocfinal = []
count = 0
temp1 = ""
temp2 = ""
while i < len(oc):
    i += 2
i = 0
while i < len(oc):
    if len(oc[i]) == 1:
        i += 1
        continue
    temp1 = oc[i]
    count += 1
    temp2 = oc[i + 1]
    j = 0
    while j < len(oc[i+1]) - 1:
        ocfinal.append(temp1)
        ocfinal.append(temp2[j:j+2])
        temp1 = temp1.strip()
        temp1 = hex(int(temp1,16) + 1)
        temp1 = str(temp1)
        temp1 = temp1[2:]
        temp1 = temp1.zfill(6)
        temp1 = temp1.upper()
        j += 2
    i += 2
i = 0
k = 0
temp = 0
while i < len(ocfinal):
    flag = 0
    mini = ocfinal[i]
    k = i + 2
    while k < len(ocfinal):
        if ocfinal[k] < mini:
            mini = ocfinal[k]
            lo = k
            flag = 1
        k += 2
    if flag == 1:
        temp2 = ocfinal[i]
        ocfinal[i] = ocfinal[lo]
        ocfinal[lo] = temp2
        temp2 = ocfinal[i+1]
        ocfinal[i+1] = ocfinal[lo+1]
        ocfinal[lo+1] = temp2
    i += 2

