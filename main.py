#Создание рандомного массива
import random

m = int(input('m = '))
minl = int(input('min_limit= '))
maxl = int(input('max_limit= '))
mass = [random.randint(minl,maxl) for i in range(m)]
print(mass)

#Бинарный поиск
val = int(input('Искомое: '))
def BinarySearch(mass, val):
    first = 0
    last = len(mass)-1
    index = -1
    mass.sort()
    print(mass)
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if mass[mid] == val:
            index = mid
        else:
            if val<mass[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print('Бинарный поиск:')
print(BinarySearch(mass, val))

#Фибоначчи
def FibonacciSearch(mass, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(mass)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(mass)-1))
        if (mass[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (mass[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(mass)-1) and mass[index+1] == val):
        return index+1;
    return -1

print('Фибоначчи:')
print(FibonacciSearch(mass, val))

#Интерполляционный
def interpolationSearch(mass, val):
    low = 0
    high = (len(mass) - 1)
    while low <= high and val >= mass[low] and val <= mass[high]:
        index = low + int(((float(high - low) / (mass[high] - mass[low])) * (val - mass[low])))
        if mass[index] == val:
            return index
        if mass[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1

print('Интерполяционный:')
print(interpolationSearch(mass, val))

#print('------------------------------------Задание 3------------------------------------')
