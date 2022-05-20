name_file = input('input name file with array: ')
file = open(name_file, 'r', encoding='utf-8')
# file = open(r'C:\Users\Tim\PycharmProjects\Python_Basic\array.txt', 'r', encoding='utf-8')
array = []
while True:
    element = file.readline()
    if element == '':
        break
    array.append(int(element))

average = (sum(i for i in array)) // len(array)

print(sum(abs(v - average) for v in array))
