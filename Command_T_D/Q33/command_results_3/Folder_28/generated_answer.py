import re
def return_vowels(s):
    return [i for i in range(41, 50) if re.match(r'[aeiou]', s[i])]
