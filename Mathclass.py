clas_1 = int(input('Введите количество учащихся в первом классе: '))
clas_2 = int(input('Введите количество учащихся во втором классе: '))
clas_3 = int(input('Введите количество учащихся в третьем классе: '))

check_1 = clas_1 % 2
clas_1 = (clas_1 // 2) + check_1

check_2 = clas_2 % 2
clas_2 = (clas_2 // 2) + check_2

check_3 = clas_3 % 2
clas_3 = (clas_3 // 2) + check_3

sum_clas = clas_1 + clas_2 + clas_3

print('\n',"\bКоличество парт которое нужно закупить: ",sum_clas)