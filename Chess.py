x1 = int(input('Пожалуйста введите цифру вертикали первой клетки:  \n --->'))
y1 = int(input('Пожалуйста введите цифру горизонтали первой клетки, где a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8: \n --->'))
x2 = int(input('Пожалуйста введите цифру вертикали второй клетки:  \n --->'))
y2 = int(input('Пожалуйста введите цифру горизонтали второй клетки, где a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8: \n --->'))

# Первый метод

rx = abs(x1-x2)
ry = abs(y1-y2)
if rx == 1 and ry == 2 or rx == 2 and ry == 1:
    print ('Ход возможный')
else:
    print('Ход невозможный')



# Второй метод

if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
    if 1 <= x1 <= 6:
        beg_0 = x1+2
        if beg_0 == x2:
            if 1 <= y1 <= 8:
                beg_2 = y1 + 1
                beg_3 = y1 - 1
                if y2 == beg_2 or y2 == beg_3:
                    print('Ход возможный')

    if 2 <= x1 <= 8:
        bbeg_0 = x1-2
        if bbeg_0 == x2:
            if 1 <= y1 <= 8:
                bbeg_2 = y1 + 1
                bbeg_3 = y1 - 1
                if y2 == bbeg_2 or y2 == bbeg_3:
                    print('Ход возможный')

    if 1 <= y1 <= 6:
        end_0 = y1+2
        if end_0 == y2:
            if 1 <= x1 <= 8:
                end_2 = x1 + 1
                end_3 = x1 - 1
                if x2 == end_2 or x2 == end_3:
                    print('Ход возможный')

    if 2 <= y1 <= 8:
        endd_0 = y1 - 2
        if endd_0 == y2:
            if 1 <= x1 <= 8:
                endd_2 = x1 + 1
                endd_3 = x1 - 1
                if x2 == endd_2 or x2 == endd_3:
                    print('Ход возможный')
else:
    print('Ход невозможный')