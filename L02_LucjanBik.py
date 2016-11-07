def mean(*x):
    """Zwraca średnią liczb podanych jako argumenty pozycyjne"""
    suma = 0; size = len(x)
    for x in x:
        suma += x
    return suma/size

# print(mean(1, 2, 3) == 2)
# print(mean(2, 2, 4, 4) == 3)
# print(mean(1, 2, 3, 4, 5, 61, 2, 12, 123, 123) == 33.6)


def check_dictionary_content(d, **param):
    """Sprawdza, czy w danym słowniku znajduje się conajmniej podana liczba elementów"""
    for key, value in param.items():
        if d.get(key, 0) < value:
            return False
    return True

# d = {'orange': 3, 'apple': 1, 'dogs': 10}
# print(check_dictionary_content(d, orange=2) == True)
# print(check_dictionary_content(d, orange=2, apple=1) == True)
# print(check_dictionary_content(d, dogs=11) == False)
# print(check_dictionary_content(d, dogs=9, cats=0) == True)
# print(check_dictionary_content(d, apple=0, cats=1) == False)
# print(check_dictionary_content(d, **d) == True)


def even_numbers_from_list(data):
    """Zwraca podlistę "data" zawierającą wyłącznie parzyste liczby"""
    return [e for e in data if e % 2 == 0]

# print(even_numbers_from_list([1, 2, 3, 4]) == [2, 4])
# print(even_numbers_from_list(range(10)) == [0, 2, 4, 6, 8])
# print(even_numbers_from_list(range(1000)) == list(range(0, 1000, 2)))
# print(even_numbers_from_list([10, 2, 3, 4, 6, -3, -4]) == [10, 2, 4, 6, -4])


def words_analyze(words):
    """Zwraca listę trójek, gdzie i'ta trójka to (i, i'te słowo, długość i'tego słowa)"""
    return [(index, word, len(word)) for index, word in enumerate(words)]

# print(words_analyze(['tomek', 'jadzia']) == [(0, 'tomek', 5), (1, 'jadzia', 6)])
# print(words_analyze([]) == [])


def count_words_starting_with_given_letter(text, letter):
    """Zwraca słownik gdzie kluczami są wszystkie słowa występujące w tekście
    rozpoczynające się na zadaną literę, a wartością ile razy wystąpiy"""

    return {word : text.count(word) for word in text.split(' ') if word[0] == letter}

# print(count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'o') == {'ola': 2, 'o': 1})
# print(count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'k') == {'kota': 1})
# print(count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'x') == {})
