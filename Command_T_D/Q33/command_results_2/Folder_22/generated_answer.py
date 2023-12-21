 
import re
def return_vowels(s):
    return re.findall(r'[A-Z][^KZ]', s)
