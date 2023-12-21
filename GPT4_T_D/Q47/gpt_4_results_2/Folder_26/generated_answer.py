
import string

def palindromes_of_specific_lengths(string_value):
    palindrome_set = set()
    for length in range(21, 32):
        for i in range(24, 85 - length + 1):
            temp_substring = string_value[i:i+length]
            if temp_substring == temp_substring[::-1] and temp_substring.isalpha():
                palindrome_set.add(temp_substring.lower())
    return palindrome_set
