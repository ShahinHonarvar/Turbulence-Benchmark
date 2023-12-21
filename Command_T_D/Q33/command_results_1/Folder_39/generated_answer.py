import re
def return_vowels(s):
    return [x for x in range(32, 97) if x > 'Q' and x <= 'z' and re.search(r'[aeiou]', chr(x), re.I)]
