import re
def return_vowels(s):
    return [ch for ch in range(45,76,1) if ch>='b' and ch<='z' and re.match(r'[aeiou]', s[ch-45:ch+1])]
