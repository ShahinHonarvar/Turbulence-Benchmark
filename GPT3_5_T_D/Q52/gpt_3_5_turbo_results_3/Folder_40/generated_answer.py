
import string

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-2):
        sub_str = string[i:i+3]
        if sub_str == sub_str[::-1] and sub_str.isalpha():
            palindromes.add(sub_str)
    return palindromes
