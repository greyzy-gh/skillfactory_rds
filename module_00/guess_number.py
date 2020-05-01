import numpy as np
#=============================================
number = np.random.randint(1,101)
# print(number)

#=============================================
# Задаем счетчик и начальные условия диапазона
count = 0
left, right = 1, 100

#=============================================
# идем по пути отбрасывания половины
while True:
    current = (left+right)//2
    if number == current:
        break
    elif number > current:
        left = current + 1
    else:
        right = current - 1
    count +=1
#=============================================
print(count)