def to_upper(input_string):
    ''' Функция выводит все заглавными '''
    return input_string.upper()

def capitalize_first_letters(input_string):
    '''делает заглавными первые буквы каждого слова в строке'''
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)