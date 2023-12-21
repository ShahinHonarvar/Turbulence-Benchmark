
import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('[a-zA-Z]+')
    string = ''.join(re.findall(pattern, string)).lower()
    palindromes_set = set()
    
    for i in range(len(string) - 99):
        substring = string[i:i+100]
        if substring == substring[::-1]:
            palindromes_set.add(substring)
    
    return palindromes_set
