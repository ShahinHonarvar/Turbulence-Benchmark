 
import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 48):
        substring = string[i:i+49]
        palindrome_substring = re.sub('[^A-Za-z]', '', substring).lower()
        if palindrome_substring == palindrome_substring[::-1]:
            palindromes.add(palindrome_substring)
    return palindromes
