import re
def return_vowels(s):
    return [i for i in range(133, 306) if re.search(r'[aeiou]', s[i:])]
