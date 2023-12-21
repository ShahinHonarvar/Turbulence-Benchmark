
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    palindromes = set()
    string_length = len(s)
    for length in range(95, string_length + 1):
        for i in range(0, string_length - length + 1):
            substring = s[i: i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
