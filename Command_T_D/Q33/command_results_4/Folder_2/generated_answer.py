import re
def return_vowels(s):
    if not s:
        return []
    for i in range(170, 645):
        if i > ord('E') and i <= ord('~'):
            if re.fullmatch(chr(i), s[i-170:i+1]):
                return [i]
    return []
