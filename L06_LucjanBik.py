# Hangman
import re
import sys
import random

class HangmanGame:

    def __init__(self, filename, max_mistakes):
        # inicjujemy gre
        self.filename = filename
        self.max_mistake = max_mistakes
        self.mistake = 0
        self.passwords = self.validate_content_file()
        self.password = ''
        self.board = []
        self.splitted_password = []



    def validate_content_file(self):
        passwords = []
        passwordCompiler = re.compile("^[a-zA-Z]+$")
        with open(self.filename, 'r') as words:
            for line in words:
                if passwordCompiler.match(line):
                    line = line[:-1]
                    passwords.append(line)
                else:
                    raise Exception('file contains invalid format of password, see: ' + line)
        return passwords

    def get_password(self):
        return self.password

    def get_board(self):
        return self.board

    def get_mistakes(self):
        return self.mistake

    def get_max_mistake(self):
        return self.max_mistake

    def get_guessed_characters(self):
        return list(filter(lambda char: char != '_', self.board))

    def start(self):
        index = random.randint(0, len(self.passwords) - 1)
        self.password =  self.passwords.__getitem__(index)
        self.board = ['_' for x in range(len(self.password))]
        self.splitted_password = list(self.password)

    def start(self, new_password):
        self.password = new_password
        self.board = ['_' for x in range(len(self.password))]
        self.splitted_password = list(self.password)

    def get_word_length(self):
        return len(self.password)

    def all_chars_are_guessed(self):
        for i, char in enumerate(self.board):
            if char == '_':
                return False
        return True


    def finished(self):
        # finished() zwraca True gdy gra sie zakonczyla
        if self.mistake >= self.max_mistake or self.all_chars_are_guessed():
            return True
        else:
            return False

    def guess(self, char):
        # zgadujemy litere, .guess powinno zwrocic liste pozycji gdzie 'a' wystepuje
        charCompiler = re.compile("^[a-zA-Z]$")

        if (not charCompiler.match(char)):
            raise Exception("invalid input, game expects single character!")

        if (self.mistake >= self.max_mistake):
            raise Exception("You made to many mistakes!")

        finded_positions = []
        for index in range(0, len(self.password)):
            if self.splitted_password[index] == char:
                self.board[index] = char
                finded_positions.append(index)

        if len(finded_positions) == 0:
            self.mistake = self.mistake + 1

        return finded_positions


    def did_I_win(self):
        # True jesli wygralismy, False w przeciwnym przypadku
        for i, char in enumerate(self.board):
            if char == '_':
                return False
        return True

class HangmanAI(object):

    def __init__(self, dictionary, max_mistakes):
        self.filename = dictionary
        self.board = []
        self.invalid_characters = []
        self.max_mistakes = max_mistakes
        self.mistakes = 0
        self.all_passwords = self.validate_content_file()
        self.possible_passwords = []



    def start(self, length):  # podajemy dlugosc slowa
        self.clear_prevoius_state()
        self.match_password_by_length(length)



    def get_guess(self):  # zwraca litere ktora powinniśmy zgadywac
        pass

    def update_response(self, response):  # robimy cos z odpowiedzia gry
        pass

    def clear_prevoius_state(self):
        self.board = []
        self.invalid_characters = []
        self.mistakes = 0
        self.possible_passwords = []

    def match_password_by_length(self, length):
        for password in self.all_passwords:
            if len(password) == length:
                self.possible_passwords.append(password)

    def validate_content_file(self):
        passwords = []
        passwordCompiler = re.compile("^[a-zA-Z]+$")
        with open(self.filename, 'r') as words:
            for line in words:
                if passwordCompiler.match(line):
                    line = line[:-1]
                    passwords.append(line)
                else:
                    raise Exception('file contains invalid format of password, see: ' + line)
        return passwords


# game = HangmanGame('slownik.txt', max_mistakes=6) # inicjujemy gre
game = HangmanGame('valid_slownik.txt', max_mistakes=6) # inicjujemy gre
# game.start() # losujemy slowo
game.start("credentials") # losujemy slowo
print(game.get_password())

print('Slowo ma', game.get_word_length(), 'liter') # pobieramy dlugosc wylosowanego slowa


guessed_characters = []
bad_guess = []
while not game.finished():  # finished() zwraca True gdy gra sie zakonczyla
    print("Guess a letter: ")
    userinput = sys.stdin.readline().rstrip('\n')

    guess = game.guess(userinput)
    if len(guess) == 0:
        bad_guess.append(userinput)
        print(bad_guess)
        print("bad guesses " + str(game.get_mistakes()) + "/" + str(game.get_max_mistake()) + " " + str(guessed_characters))
    else:
        guessed_characters.append(guess)
        print("good guesses " + str(game.get_mistakes()) + "/" + str(game.get_max_mistake()) + " " + str(guessed_characters))


    print(game.get_board())


print(game.did_I_win())  # True jesli wygralismy, False w przeciwnym przypadku