import re
def return_vowels(s):
    return [i for i in range(4,8) if any(x.lower() in 'aeiou' for x in s[i:j])]
