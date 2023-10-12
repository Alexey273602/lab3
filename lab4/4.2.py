from string import ascii_uppercase


class Alphabet:
    def __init__(self, lang, letters=[]):
        self.lang = lang
        self.letters = letters

    def print(self):
        for i in self.letters:
            print(i, end=' ')
        print("")

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 0

    def __init__(self):
        super().__init__('En', list(ascii_uppercase))
        EngAlphabet.__letters_num = self.letters_num()

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            print(f"{letter} является буквой английского алфавита")
        else:
            print(f"{letter} не является буквой английского алфавита")

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print("Пример текста на английском языке: 'I love python' ")


abc = Alphabet('ru', ['а', 'б'])
abc.print()
print(abc.letters_num())
enAbc = EngAlphabet()
enAbc.print()
enAbc.is_en_letter('F')
enAbc.is_en_letter('Я')
enAbc.example()
