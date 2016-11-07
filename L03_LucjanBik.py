# zadanie 1
import types
import functools


def natural_numbers(k=0):
    """Tworzy generator liczb naturalnych od liczby k"""
    if k < 0:
        k=0
    while True:
        yield k
        k+=1

print(isinstance(natural_numbers(), types.GeneratorType))

for i, n in enumerate(natural_numbers()):
    print(i, i == n)
    if i > 20:
        break

for i, n in enumerate(natural_numbers(1)):
    print(i, i + 1 == n)
    if i > 20:
        break


def factorials():
    """Tworzy generator kolejnych silnii"""
    count = 1
    fact = 1
    while 1:
        yield fact
        count = count + 1
        fact = fact * count

print(isinstance(factorials(), types.GeneratorType))

results = [1, 2, 6, 24, 120, 720, 5040]
for truth, answer in zip(results, factorials()):
    print(truth, truth == answer)


# zadanie 2


def celsius_to_fahrenheit(x):
    """Konwertuje liste temperatur w stopniach Celsjusza do skali Fahrenheita"""
    return list(map(lambda c: c * 1.8 + 32, x))


print(celsius_to_fahrenheit([0, 10, 100]) == [32.0, 50.0, 212.0])
print(celsius_to_fahrenheit([-123, 0]) == [-189.4, 32.0])


def product_greater_than(x, k=0):
    """Zwraca iloczyn liczb w liście x większych od k"""
    return functools.reduce((lambda x, y: x * y), filter(lambda number: number > k, x))


print(product_greater_than([1, 2, 3]) == 6)
print(product_greater_than([1, 2, 3], 2) == 3)
print(product_greater_than([-4, 5, 10, 23, 123], -5) == -565800)


def create_sentence(x, k=0):
    """Łączy słowa (o długości co najmniej k) z listy x w zdanie"""
    return functools.reduce(lambda word1, word2: word1 + " " + word2, filter(lambda word: len(word) >= k, x))


print(create_sentence(['ala', 'ma', 'kota']) == 'ala ma kota')
print(create_sentence(['ala']) == 'ala')
print(create_sentence(['ala', 'ma', 'pieknego', 'kota'], k=3) == 'ala pieknego kota')

#zadanie 3

import sys
sys.float_info.epsilon  # epsilon maszynowy


def derivate(epsilon=None):
    """
    zwraca pochodną funkcji w punkcie, wg. wzoru f'(x) = [f(x+h) - f(x)]/h,
    gdzie h jest parametrem dekoratora, jeśli nie zostanie podany, należy przyjąć 1000 * epsilon maszynowy
    """
    def derivate_decorator(f):
        def func_wrapper(val):
            h = 1000 * sys.float_info.epsilon if epsilon is None else epsilon
            return (f(val+h) - f(val))/h
        return func_wrapper
    return derivate_decorator

@derivate(0.01)
def f(x):
    return x * x


@derivate(0.00001)
def g(x):
    return x * x * x + 3


def test(a, b, eps=1):
    return abs(round(a) - round(b)) < eps

print(test(f(100), 200.0))
print(round(f(0)) == 0.0)

print(test(g(100), 30000.0))
print(round(g(0)) == 0.0)



from random import random

for x in [random() * 1000. for _ in range(20)]:
    print(f(x), 2 * x, test(f(x), 2 * x))
    print(g(x), 3 * x ** 2, test(g(x), 3 * x ** 2))

import copy
class FrozenDictionary(object):
    """
    Odpowiednik frozenset dla zbiorów, czyli słownik, który nie jest modyfikowalny,
    a dzięki temu może być np. elementem zbiorów, albo kluczem w innym słowniku.
    """

    def __init__(self, dictionary):
        """Tworzy nowy zamrożony słownik z podanego słownika"""
        self.dict = copy.deepcopy(dictionary)

    def __hash__(self):
        """Zwraca hasz słownika (int)"""
        return hash(frozenset(self.dict))

    def __eq__(self, d):
        """Porównuje nasz słownik z zamrożonym słownikiem d"""
        return self.dict == d

    def __repr__(self):
        """Zwraca reprezentację naszego słownika jako string"""
        return str(self.dict)


dicts = [FrozenDictionary({'ala': 4}), FrozenDictionary({'ala': 1, 'jacek': 0}), \
         FrozenDictionary({'ala': 4}), FrozenDictionary({'ala': 2}), FrozenDictionary({'jacek': 0, 'ala': 1})]

s = set(dicts)
print(dicts[0] == dicts[2])
print(dicts[0] != dicts[3])
print(len(s) == 3)
for d in dicts:
    print(d in s)

# Powinno wyświetlić coś w stylu set([{'ala': 4}, {'ala': 1, 'jacek': 0}, {'ala': 2}])
print(s)
