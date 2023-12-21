
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower() # convert string to lowercase
    palindromes = set()
    
    for i in range(len(string)):
        for j in range(i + 68, len(string) + 1):
            sub_str = string[i:j] # get substring
            if sub_str == sub_str[::-1]: # check if substring is a palindrome
                palindromes.add(sub_str) # add palindrome to set
    
    return palindromes
