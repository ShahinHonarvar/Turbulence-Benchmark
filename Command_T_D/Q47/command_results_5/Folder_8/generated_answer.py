 
import re
def palindromes_of_specific_lengths(s):
    return re.findall(r"<(?=a)[a-z]{50}(?<=a)>", s, flags=re.I)
