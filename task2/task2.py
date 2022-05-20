from math import sqrt


def point_in_cicle(x, y, xr, yr, r):
    h = sqrt((x - xr) ** 2 + (y - yr) ** 2)

    if h > r:
        print("точка находится за пределами круга")
    elif h < r:
        print("точка принадлежит кругу")
    else:
        print("точка на границе круга")


name_file = input('input name file with coordinates center of the circle and radius : ')
file = open(name_file, 'r', encoding='utf-8')
# file = open(r'координаты круга и радиус.txt', 'r', encoding='utf-8')
text = file.read()
xr, yr, r = map(float, text.split())
file.close()

name_file = input('input name file with point coordinates: ')
file = open(name_file, 'r', encoding='utf-8')
# file = open(r'координаты точек.txt', 'r', encoding='utf-8')

x = []
y = []
i = 0

while True:
    line = file.readline()
    if line == '':
        break

    x1, y1 = line.split()
    x.append(float(x1))
    y.append(float(y1))

    print(i, end=' - ')
    point_in_cicle(x[i], y[i], xr, yr, r)
    i += 1

file.close()
