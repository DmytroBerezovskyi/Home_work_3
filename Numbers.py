numbers = int(input('Введите целое, положительное, ТРЁХЗНАЧНОЕ число: '))
number_last = numbers % 10
number_midl = numbers % 100
number_midl = number_midl // 10
number_beg = numbers % 1000
number_beg = number_beg // 100
number_last = str(number_last)
number_midl = str(number_midl)
number_beg = str(number_beg)
numbers_revert = number_last+number_midl+number_beg
print(numbers_revert)
