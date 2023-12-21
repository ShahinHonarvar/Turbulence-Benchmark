import re
def return_vowels(s):
    return [i for i in range(8, 9) if i in s and re.search(r'[aeiouy]', s[i:])]
