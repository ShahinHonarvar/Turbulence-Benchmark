
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)):
        for j in range(i+4, len(string)+1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1] and re.match("^[a-zA-Z]+$", sub_string):
                palindromes.add(sub_string)
    
    return palindromes
