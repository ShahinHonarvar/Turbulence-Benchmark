
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-150+1):
        sub_string = string[i:i+150]
        if sub_string == sub_string[::-1] and re.match('^[a-zA-Z]+$', sub_string):
            palindromes.add(sub_string)
    return palindromes
