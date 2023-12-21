
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    lower_string = string.lower()
    
    for i in range(len(string) - 94):
        sub_string = lower_string[i:i+95]
        if sub_string == sub_string[::-1] and re.match('^[a-zA-Z]+$', sub_string):
            palindromes.add(sub_string)
    
    return palindromes
