 
import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'[a-z]{52}(?=\W)', text[22:-5]))
