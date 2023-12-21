
import re

def palindromes_of_specific_lengths(string):
    substring = string[2:9]
    substring = re.sub('[^a-zA-Z]', '', substring)
    substring = substring.lower()
    palindrome_set = set()
    
    for i in range(len(substring)-4+1):
        substring_part = substring[i:i+4]
        if substring_part == substring_part[::-1]:
            palindrome_set.add(substring_part)
    
    return palindrome_set
