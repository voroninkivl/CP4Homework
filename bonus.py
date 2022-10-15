mas=[]
count=0
size=float(input("Введите количество чисел в массиве: "))
while size-size//1!=0 or size<=0:
    if size-size//1!=0:
        print("Введите целое число!")
    if size<=0:
        print("Вы ввели 0 или отрицательное число для размера массива!")
    size=float(input("Введите количество чисел в массиве: "))

size=int(size)
delta=int(input("Введите DELTA: "))
for i in range(size):
    mas.append(int(input("Введите число: ")))
mini=mas[0]
for m in mas:
    if m<mini:
        mini=m
for i in mas:
    if i-mini==delta:
        count+=1
print("Количество элементов, отличающихся от минимального на DELTA: ",count)
