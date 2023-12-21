import re
def return_vowels(s):
    return [ch for ch in range(149, 313) if ch in s and ch.isupper() and ch.isalpha() and ch.isalnum() and ch > 'M' and ch <= 'j']
