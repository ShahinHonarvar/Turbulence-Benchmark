
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    
    for i in range(len(string)):
        for j in range(i + 14, len(string) + 1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    
    return palindromes
