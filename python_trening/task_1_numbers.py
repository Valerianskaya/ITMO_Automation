a = 2
print(a, "относится к типу" , type(a))

b = 15.0001
print(b, "относится к типу" , type(b))

c = 1+2j
print(c, "комплексное число?", isinstance(c, complex))
print(6 + 2) # 8
print(6 - 2) # 4
print(6 * 2) # 12
print(6 / 2) # 3.0

print(7 / 2) # 3.5
print(7 // 2) # Получение целого числа от деления. Резуотат - 3

print(7 % 2) # Получение  остатка от деления числа 7 на 2. Результат - 1

print (6 ** 2)


s = "Это строка"
print (s + '\n')
g = '''Многострочная строка'''
print(g + '\n')
print('Строки ' + 'можно ' + 'складывать')

print( 'Auto' * 3)

print(len('test'))

a = 'Auto'
print(a[0]) # A
print(a[ -2]) # t