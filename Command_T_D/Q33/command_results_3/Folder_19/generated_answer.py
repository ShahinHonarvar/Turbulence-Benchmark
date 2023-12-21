import re
def return_vowels(s):
    return [i for i in range(51, 77) if re.search(r'[aeiou]', s[4:])]
