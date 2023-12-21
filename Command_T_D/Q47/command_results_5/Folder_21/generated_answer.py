 
import re
def palindromes_of_specific_lengths(text):
    return re.findall(r'[a-z]{1,5}(?=([a-z]{%d,%d}))[a-z]{%d,%d}[a-z]{%d,%d}'.format(100, 295, 136, 160), text.lower())
