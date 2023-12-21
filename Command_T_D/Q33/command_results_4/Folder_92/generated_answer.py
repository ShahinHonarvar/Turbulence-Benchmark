import re
def return_vowels(s):
    return [x for x in range(ord('a') + 3, ord('e') + 1) if re.search(r'[aeiou]([a-d])', s)]
