def search4vowels (phrase:str) -> set:
    '''Возвращает множество гласных найденных в фразе'''
    return set('aeiou').intersection(set(phrase))

def search4letters (phrase:str, letters:str = 'aeiou') -> set:
    '''Возвращает множество букв найденных в ФРАЗЕ, буквы по умолчанию 'aeiou' '''
    return set(letters).intersection(set(phrase))