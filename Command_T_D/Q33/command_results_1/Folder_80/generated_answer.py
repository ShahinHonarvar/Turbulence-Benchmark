import re
def return_vowels(s):
    for i in range(85, 99):
        if s[i] in re.compile(r'[aeiou]'):
            yield s[i]
    return
