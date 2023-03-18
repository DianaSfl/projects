import random
import string
class HelpFunctions:
    @staticmethod
    def Digits(pwd_digits, characters):
        if pwd_digits == 'y':
            numbers_random = ''.join(random.choice(string.digits) for i in range(characters))
            return numbers_random
        return ''

    @staticmethod
    def Uppercase(pwd_uppercase, characters):
        if pwd_uppercase == 'y':
            upper_random = ''.join(random.choice(string.ascii_uppercase) for i in range(characters))
            return upper_random
        return ''

    @staticmethod
    def Lowercase(pwd_lowercase, characters):
        if pwd_lowercase  == 'y':
            lower_random = ''.join(random.choice(string.ascii_lowercase) for i in range(characters))
            return lower_random
        return ''

    @staticmethod
    def Symbols(pwd_punctuation, characters):
        if pwd_punctuation == 'y':
            symbol_random = ''.join(random.choice(('!#$%&*+-=?@^_')) for i in range(characters))
            return symbol_random
        return ''

    @staticmethod
    def CreateGenerator(line, characters):
        password = ''.join(random.choice((line)) for i in range(characters))
        return password