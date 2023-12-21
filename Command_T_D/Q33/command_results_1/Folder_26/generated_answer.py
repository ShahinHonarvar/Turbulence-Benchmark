 
import re
def return_vowels(s):
    return re.findall(r'[aeiou]{10,82}', s)[::-1][1:-1]
