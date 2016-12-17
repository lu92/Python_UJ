class BagOfWords:
    @staticmethod
    def load_text(text):
        if type(text) is str:
            words = text
        else:
            with text as f:
                words = f.read()
        return words.split(" ")

    def __init__(self, text):
        words = self.load_text(text)
        self.dictionary = []
        used = []
        for word in words:
            if word not in used:
                self.dictionary.append((words.count(word), word))
                used.append(word)

    def __str__(self):
        text = ""
        for num, word in self.dictionary:
            text += word + ":" + str(num) + ", "
        return text[:-2]

    def __iter__(self):
        s = list(reversed(sorted(self.dictionary)))
        for _, word in s:
            yield word

    def __add__(self, other):
        new_dictionary = []
        for num, word in self.dictionary:
            if word not in other:
                new_dictionary.append((num, word))
            else:
                new_dictionary.append((num + other[word], word))
                other.dictionary.remove((other[word], word))
        new_dictionary += other.dictionary
        new_bag = BagOfWords("")
        new_bag.dictionary = new_dictionary
        return new_bag

    def __getitem__(self, item):
        for num, word in self.dictionary:
            if item == word:
                return num

    def __setitem__(self, key, value):
        for idx, (num, word) in enumerate(self.dictionary):
            if key == word:
                self.dictionary[idx] = (value, key)

class SetOfWords(BagOfWords):
    def __init__(self, text):
        super().__init__(text)
        self.dictionary = [word for _, word in self.dictionary]

    def __str__(self):
        text = ""
        for word in self.dictionary:
            text += word + ", "
        return text[:-2]
