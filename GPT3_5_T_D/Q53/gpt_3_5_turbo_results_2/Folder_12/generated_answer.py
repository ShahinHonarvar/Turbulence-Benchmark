
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            sub_string = string[i:j+1]
            
            if len(sub_string) >= 51 and re.match("^[a-zA-Z]*$", sub_string):
                if sub_string == sub_string[::-1]:
                    palindromes.add(sub_string)
                    
    return palindromes
