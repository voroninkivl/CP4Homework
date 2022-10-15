mas1=[]
mas2=[]
size1=float(input("Введите количество чисел в массиве 1: "))
if size1<=0 or size1-size1//1!=0:
    while size1-size1//1!=0 or size1<=0:
        if size1-size1//1!=0:
            print("Введите целое число!")
        if size1<=0:
            print("Вы ввели 0 или отрицательное число!")
        size1=float(input("Введите количество чисел в массиве 1: "))
size2=float(input("Введите количество чисел в массиве 2: "))
if size2<=0 or size2-size2//1!=0:
    while size2-size2//1!=0 or size2<=0:
        if size2-size2//1!=0:
            print("Введите целое число!")
        if size2<=0:
            print("Вы ввели 0 или отрицательное число!")
        size2=float(input("Введите количество чисел в массиве 2: "))

size1=int(size1)
size2=int(size2)
for i in range(size1):
    mas1.append(float(input("Введите число в массив 1: ")))
for i in range(size2):
    mas2.append(float(input("Введите число в массив 2: ")))
common=[]
if len(mas1)>=len(mas2):
    for i in range(0,len(mas1)):
        if mas1[i] in mas2:
            if mas1[i] not in common:
                common.append(mas1[i])
else:
    for i in range(0,len(mas2)):
        if mas2[i] in mas1:
            if mas1[i] not in common:
                common.append(mas2[i])
if len(common)<1:
    print("У массивов нет общих элементов :(")
else:
    print("Элементы, которые содержаться в обоих массивах: ",common)
