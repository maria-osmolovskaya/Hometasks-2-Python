#На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint 
n = int (input("Введите количество монеток: "))
count=0
list = []
for i in range (n):
    list.append(randint(0,1))
    if list[i] == 0:
        count+=1
print(list)
if count < n//2:
    print(count)
else:
    print(n-count)
