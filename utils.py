import time


def string_capital(mon_texte):
    if not isinstance(mon_texte, str):
        raise TypeError('Please provide a string argument')
    return mon_texte.upper()


def divide(x, y):
    return x/y


def string_to_array(texte):
    return texte.split(',')
