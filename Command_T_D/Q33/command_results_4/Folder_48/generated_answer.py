import re
def return_vowels(s):
    return [ch for ch in range(529, 828) if re.match(r'[aeiou]', s[ch])]
