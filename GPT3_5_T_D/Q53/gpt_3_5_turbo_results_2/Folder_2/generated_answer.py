
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    string = re.sub('[^a-zA-Z]+', '', string)
    
    for i in range(len(string)):
        for j in range(i+55, len(string)+1):
            sub_str = string[i:j]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
                
    return palindromes
