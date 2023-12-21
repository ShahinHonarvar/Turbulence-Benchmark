
import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)-55):
        substring = string[i:i+56]
        if re.match('^[a-zA-Z]+$', substring):
            reversed_substring = substring[::-1]
            if substring.lower() == reversed_substring.lower():
                palindromes.add(substring)
    return palindromes
