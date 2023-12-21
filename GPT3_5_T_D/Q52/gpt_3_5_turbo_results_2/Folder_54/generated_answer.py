
import re

def palindrome_of_length_n(string):
    length = 85
    string = re.sub("[^a-zA-Z]+", "", string.lower())
    palindromes = set()
    
    for i in range(len(string) - length + 1):
        sub_string = string[i:i+length]
        if sub_string == sub_string[::-1]:
            palindromes.add(sub_string)
            
    return palindromes
