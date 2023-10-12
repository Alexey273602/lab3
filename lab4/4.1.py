class String:
    def __init__(self, str):
        self.str = str

    def length(self):
        return len(self.str)

    def __add__(self, other):
        return self.str + other

    def reverse(self):
        return self.str[::-1]

    def upper_case(self):
        return self.str.upper()

    def lower_case(self):
        return self.str.lower()

    def is_equal(self, str1):
        if (self.str == str1):
            return True
        else:
            return False


c = String("Я люблю")
print(c.length())
print(c + " питон")
print(c.reverse())
print(c.upper_case())
print(c.lower_case())
print(c.is_equal("Я люблю"))
print(c.is_equal("Я не люблю"))
