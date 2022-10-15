mass=[]
num=float(input("Введите количество чисел в массиве: "))
while num-num//1!=0 or num<=0:
    if num-num//1!=0:
        print("Введите целое число!")
    if num<=0:
        print("Вы ввели 0 или отрицательное число!")
    num=float(input("Введите количество чисел в массиве: "))

num=int(num)
for x in range(num):
    mass.append(float(input("Введите число с плавающей точкой ")))
maxx=mass[0]
for i in mass:
    if i>maxx:
        maxx=i
mass=mass[:mass.index(maxx) + 1] + [0]*(len(mass)- len(mass[:mass.index(maxx) + 1]))
print(mass)
