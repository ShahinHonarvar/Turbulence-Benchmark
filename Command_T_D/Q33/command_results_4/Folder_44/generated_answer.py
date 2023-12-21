 
import re
def return_vowels(s):
    return [m for m in re.finditer(r'[aeiou]', s[46:49]) if m.group()]
