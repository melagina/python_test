
#int
number = 5
#float
fnumber = 5.7
#str
name = "masha"
name = 'kisa'
#bool
status = True
status = False
#changing varible type
varable = 5
print("variable = ", varable)
varable = 'masha'
print("variable = "+ varable)

#вывод
print(name,' = ', status  )
#экранирование
print("kisa says \"meow\"")
print('kisa says "meow"')
print("kisa says 'meow'")
print('kisa says \'meow\'')
#перевод строки
print('hello\nworld')
#конкатенация
print('hello ' + name)
print(name + ' is', number, 'year old')
print(name + ' is ' + str(number) + ' year old')
print('''
multi line string
second line
''')
#Ввод значений
# name = input("say your name: ")
# age = input("say your age: ")
# print(name + ' is ' + age + " years old")
#базовые операции
# + - * / **(степень) %(деление по модулю = остаток) унарный минус (смена знака), округение, пи
a = 5

b = 10
c = a%b
#унарный минус (смена знака)
a = -a
print(a)
a = -a
print(a)
#округление
a = 5.659
print(round(a, -1))
print(round(a))
import math
print(math.floor(a))
print(math.ceil(a))
print(math.pi)
#целочисленное деление
print(5//3)

# левый сдвиг <<
print(2<<2)