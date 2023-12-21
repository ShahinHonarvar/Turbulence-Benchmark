
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string) - 23):
        sub_string = string[i:i+24]
        if re.match('^[a-zA-Z]+$', sub_string):
            is_palindrome = sub_string == sub_string[::-1]
            if is_palindrome:
                palindromes.add(sub_string)
    
    return palindromes
