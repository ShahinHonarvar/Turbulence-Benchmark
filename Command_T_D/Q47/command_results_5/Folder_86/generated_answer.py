 
import re
def palindromes_of_specific_lengths(str1):
    return set(re.findall(r"(?i)([a-z]{1,34})\1", str1[30:-5], flags=re.I))
