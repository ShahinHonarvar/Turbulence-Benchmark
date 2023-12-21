 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?=([a-z]+){1,2}18([a-z]+){38,60}87([a-z]+){1,2}))', s, flags=re.I))
