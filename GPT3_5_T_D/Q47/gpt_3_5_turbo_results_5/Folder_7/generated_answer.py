
import re

def palindromes_of_specific_lengths(string):
    substring = string[119:257].lower()
    palindromes = set()
    
    for length in range(104, 124):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i+length]
            if re.match(r'^[a-zA-Z]+$', palindrome):
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    
    return palindromes
