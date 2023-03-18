# Генератор паролей
# Программа предлагает выбрать параметры для составления необходимого пароля
def PasswordGenerator():
    pwd_length = int(input('Enter password length: '))
    pwd_digits = input('Include numbers (yes = y, no = n): ')
    pwd_uppercase = input('Include uppercase letters (yes = y, no = n): ') # заглавные буквы
    pwd_lowercase = input('Include lowercase letters (yes = y, no = n): ') # строчные буквы
    pwd_punctuation = input('Include symbols "!#$%&*+-=?@^_"? (yes = y, no = n): ')
    import HelpFunctions
    help = HelpFunctions.HelpFunctions
    digits = help.Digits(pwd_digits, pwd_length)
    upper = help.Uppercase(pwd_uppercase, pwd_length)
    lower = help.Lowercase(pwd_lowercase, pwd_length)
    punct = help.Symbols(pwd_punctuation, pwd_length)
    print(help.CreateGenerator(digits + upper + lower + punct, pwd_length))

if __name__ == '__main__':
    PasswordGenerator()