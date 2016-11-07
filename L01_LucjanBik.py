def helloworld() :
    print("hello world")

helloworld()

def sum_of_cubes(n):
    """ Funkcja powinna zwrócić sumę sześcianów liczb od 1 do n włącznie """
    i = 0; result = 0
    for i in range(1, n+1):
        result += i**3
    return result

print(sum_of_cubes(1) == 1)
print(sum_of_cubes(3) == 36)


def how_many_digits(n):
    """ Zwraca liczbę cyfr liczby n """
    if n==0:
        return 1
    digits = 0
    while n > 0:
        n = int(n / 10)
        digits += 1
    return digits

print(how_many_digits(0) == 1)
print(how_many_digits(10) == 2)
print(how_many_digits(1234567890) == 10)


def is_palindrome(word):
    """ Funkcja sprawdza czy *word* jest palindromem """
    n = len(word)
    for i, letter in enumerate(word):
        if letter != word[n-i-1]:
            return False
    return True

print(is_palindrome('ala') == True)
print(is_palindrome('ananas') == False)
print(is_palindrome('ananasa') == False)
print(is_palindrome('tomek') == False)



def how_many_different_letters(word):
    """ Zwraca liczbę unikalnych znaków w słowie, możemy założyć, że słowo składa się z małych liter alfabetu angielskiego """
    letters = 0
    for letter in ''.join(set(word)):
        letters += 1
    return letters

print(how_many_different_letters('tomek') == 5)
print(how_many_different_letters('ala') == 2)
print(how_many_different_letters('ananas') == 3)
print(how_many_different_letters('jola') == 4)


def rot13(word):
    """ Implementacja znanego szyfru ROT13 (http://pl.wikipedia.org/wiki/ROT13) dla słów z małych liter alfabetu angielskiego """
    rotated = ''
    a = ord('a') # Zwraca kod znaku, funkcją odwrotną jest chr(int)
    z = ord('z')
    for letter in word:
        rotated += chr(a+(ord(letter)+13-a) % 26)
    return rotated

print(rot13('ala') == 'nyn')
print(rot13('ananas') == 'nananf')
print(rot13('tomek') == 'gbzrx')
print(rot13('abcdefghijklmnoprstuwxyz') == 'nopqrstuvwxyzabcefghjklm')


def find_a_word_in_sentence(word, sentence):
    """ Sprawdza czy słowo wystepuje w zdaniu """
    return word in sentence.split(" ")

print(find_a_word_in_sentence('ala', 'ala ma kota') == True)
print(find_a_word_in_sentence('al', 'ala ma kota') == False)
print(find_a_word_in_sentence('ma k', 'ala ma kota') == False)
print(find_a_word_in_sentence('ma', 'ala ma kota') == True)



def how_many_integers(N):
    specialNumbers = ['0','2','7','9']
    result = 0
    for i in range(1, N):
        tmp = str(i);
        for j in tmp:
            czyDodac = True
            if j not in specialNumbers:
                 czyDodac = False
        if czyDodac == True:
            result = result + 1
    return result


print(how_many_integers(1) == 0)
print(how_many_integers(10) == 3)
print(how_many_integers(28) == 6)


