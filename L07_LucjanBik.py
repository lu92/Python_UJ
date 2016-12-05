import timeit

# print(timeit.timeit('for i in range(100000): i', number=100))
#
# print(timeit.timeit('char in text', setup='text = "sample string"; char = "g"'))
# print(timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"'))
# print(timeit.timeit('len([a==char for a in text])>0', setup='text = "sample string"; char = "g"'))
#
# # Jak szybkie sa metody laczenia stringow?
# codes = {
#     '" ".join(chars)',
#     'from functools import reduce; reduce(lambda a, b : a + " " + b, chars)',
#     'for a in chars: word += a + " ";'
# }
#
# for code in codes:
#     print(code)
#     print(timeit.timeit(code, setup='chars = ["a"] * 1000; word = ""', number=1000))
# print()

# zadanie 1

# a) Konkatenacja stałej długości stringów

codes = {
    "word=a+b+c+d",
    "word=\"%s%s%s%s\" % (a,b,c,d)",
    "word = \"{}{}{}{}\".format(a, b, c, d)"
}

print("zad 1a: ")
for code in codes:
    print(code)
    print(timeit.timeit(code, setup='a="aaa"; b="bbb"; c="ccc"; d="ddd"; word = ""', number=1000))
print()

zad1a_a = timeit.timeit("word=a+b+c+d", setup='a="aaa"; b="bbb"; c="ccc"; d="ddd"; word = ""', number=1000)
print("1a_a test: " + str(zad1a_a))

zad1a_b = timeit.timeit("word=\"%s%s%s%s\" % (a,b,c,d)", setup='a="aaa"; b="bbb"; c="ccc"; d="ddd"; word = ""', number=1000)
print("1a_b test: " + str(zad1a_b))

zad1a_c = timeit.timeit("word = \"{}{}{}{}\".format(a, b, c, d)", setup='a="aaa"; b="bbb"; c="ccc"; d="ddd"; word = ""', number=1000)
print("1a_c test: " + str(zad1a_c))

# b) Obsługa odczytywania nieistniejących kluczy w słowniku

dictionary = {"Name": "Harry", "Lastname": "Potter", "Age": 20, "FieldOfStudy": "History"}

zad1b_a = timeit.timeit('"Birth" in slownik', setup='slownik={0}'.format(dictionary), number=1000)
print("1b_a test: " + str(zad1b_a))

zad1b_b = timeit.timeit('"Birth" in slownik.keys()', setup='slownik={0}'.format(dictionary), number=1000)
print("1b_b test: " + str(zad1b_b))

zad1b_c = timeit.timeit('slownik.get("Birth", None)', setup='slownik={0}'.format(dictionary), number=1000)
print("1b_c test: " + str(zad1b_c))

zad1b_d = timeit.timeit('try:\n\tslownik["Birth"]\nexcept KeyError:\n\tpass', setup='slownik={0}'.format(dictionary), number=1000)
print("1b_d test: " + str(zad1b_d))


# c) Przekonwertuj listę słów na listę słów złożonych z wielkich liter, np. ['ala', 'ola'] -> ['ALA', 'OLA']
upper_names = []
for name in ['ala', 'ola']:
    upper_names.append(name.upper())
print(upper_names)

upper_names = []
names = ['ala', 'ola']
print([name.upper() for name in names])

print(list(map(lambda x:x.upper(),names)))

zad1c_a = timeit.timeit('upper_names = []\nfor name in names: \n\tupper_names.append(name.upper())', setup='upper_names=[]; names=["ala", "ola"];', number=1000)
print("1c_a test: " + str(zad1c_a))

zad1c_b = timeit.timeit('[name.upper() for name in names]', setup='names=["ala", "ola"];', number=1000)
print("1c_b test: " + str(zad1c_b))


zad1c_c = timeit.timeit('list(map(lambda name:name.upper(),names))', setup='names=["ala", "ola"];', number=1000)
print("1c_c test: " + str(zad1c_c))

# d) Stwórz warunkowo listę, np. listę liczb parzystych
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odds = []
for number in numbers:
    if number % 2 == 0:
        odds.append(number)
print(odds)

odds = []
print([x for x in numbers if (x % 2) == 0])

odds = []
print([x for x in filter(lambda x: x%2 ==0, numbers)])

zad1d_a = timeit.timeit('odds = [] \nfor number in numbers: \n\tif number % 2 == 0: \n\t\todds.append(number)', setup='numbers={0};'.format(numbers), number=1000)
print("1d_a test: " + str(zad1d_a))

zad1d_b = timeit.timeit('[x for x in numbers if (x % 2) == 0]', setup='numbers={0};'.format(numbers), number=1000)
print("1d_b test: " + str(zad1d_b))

zad1d_c = timeit.timeit('[x for x in filter(lambda x: x%2 ==0, numbers)]', setup='numbers={0};'.format(numbers), number=1000)
print("1d_c test: " + str(zad1d_c))


