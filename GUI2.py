from tkinter import *
from tkinter import ttk
import Linker_Loader_Store_Each_With_Relocation as l
window = Tk()
window.title("Loader")
window.geometry("1000x500")
window.config(bg='Black')
main_frame = Frame(window)
main_frame.pack(fill=BOTH, expand=1)
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame,anchor="nw")

label1 = Label(second_frame, text="Memory Address",fg='Blue',font='Courier,22')
label2 = Label(second_frame, text="Contents",fg='Blue',font='Courier,22')
label1.grid(row=0,column=0)
label2.grid(row=0,column=6)
if l.RA < l.RB:
    i = str(l.RA)
    end = hex(int(l.RB,16) + int(l.RBL,16))
else:
    i = str(l.RB)
    end = hex(int(l.RA, 16) + int(l.RAL, 16))
end = str(end)
end = end[2:]
end = end.zfill(4)
end = end.upper()
j = 1
first = ""
second = ""
third = ""
while l.ocfinal:
    i = l.ocfinal[0][:-1]
    i = hex(int(i,16) * 16)
    i = str(i)
    i = i[2:]
    i = i.zfill(4)
    i = i.upper()
    first = ""
    second = ""
    third = ""
    fourth = ""
    label3 = Label(second_frame, text=i)
    label3.grid(row=j,column=0)
    k = hex(int(i,16) + 4)
    k = k[2:]
    k = k.zfill(4)
    k = k.upper()
    while i != k:
        q = 0
        flag = 0
        while q < len(l.ocfinal):
            if i.zfill(6) == l.ocfinal[q]:
                l.ocfinal.pop(q)
                first = first + l.ocfinal.pop(q)
                flag = 1
                break
            q += 1
        if flag == 0:
            first = first + "xx"

        i = hex(int(i,16) + 1)
        i = hex(int(i, 16))
        i = i[2:]
        i = i.zfill(4)
        i = i.upper()
    label4 = Label(second_frame, text="        ")
    label4.grid(row=j, column=1)
    label5 = Label(second_frame, text=first)
    label5.grid(row=j,column=2)

    k = hex(int(i, 16) + 4)
    k = k[2:]
    k = k.zfill(4)
    k = k.upper()
    while i != k:
        q = 0
        flag = 0
        while q < len(l.ocfinal):
            if i.zfill(6) == l.ocfinal[q]:
                l.ocfinal.pop(q)
                second = second + l.ocfinal.pop(q)
                flag = 1
                break
            q += 1
        if flag == 0:
            second = second + "xx"

        i = hex(int(i, 16) + 1)
        i = hex(int(i, 16))
        i = i[2:]
        i = i.zfill(4)
        i = i.upper()
    label4 = Label(second_frame, text="        ")
    label4.grid(row=j, column=4)
    label5 = Label(second_frame, text=second)
    label5.grid(row=j, column=5)
    k = hex(int(i, 16) + 4)
    k = k[2:]
    k = k.zfill(4)
    k = k.upper()
    while i != k:
        q = 0
        flag = 0
        while q < len(l.ocfinal):
            if i.zfill(6) == l.ocfinal[q]:
                l.ocfinal.pop(q)
                third = third + l.ocfinal.pop(q)
                flag = 1
                break
            q += 1
        if flag == 0:
            third = third + "xx"

        i = hex(int(i,16) + 1)
        i = hex(int(i, 16))
        i = i[2:]
        i = i.zfill(4)
        i = i.upper()
    label4 = Label(second_frame, text="        ")
    label4.grid(row=j, column=6)
    label5 = Label(second_frame, text=third)
    label5.grid(row=j,column=7)

    k = hex(int(i, 16) + 4)
    k = k[2:]
    k = k.zfill(4)
    k = k.upper()
    while i != k:
        q = 0
        flag = 0
        while q < len(l.ocfinal):
            if i.zfill(6) == l.ocfinal[q]:
                l.ocfinal.pop(q)
                fourth = fourth + l.ocfinal.pop(q)
                flag = 1
                break
            q += 1
        if flag == 0:
            fourth = fourth + "xx"

        i = hex(int(i,16) + 1)
        i = hex(int(i, 16))
        i = i[2:]
        i = i.zfill(4)
        i = i.upper()
    label4 = Label(second_frame, text="        ")
    label4.grid(row=j, column=9)
    label5 = Label(second_frame, text=fourth)
    label5.grid(row=j,column=10)
    i = i[2:]
    i = i.zfill(4)
    i = i.upper()
    j += 1
window.mainloop()
