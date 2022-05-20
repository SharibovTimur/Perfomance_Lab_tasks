name_file = input('input name file: ')
file = open(name_file, 'r', encoding='utf-8')
text = file.read()
n, m = map(int, text.split())

file.close()
i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break
print()
