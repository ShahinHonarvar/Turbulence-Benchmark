
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]+', '', string)
    set_of_palindromes = set()
    for i in range(len(string)):
        for j in range(i + 59, len(string) + 1):
            substring = string[i:j]
            is_palindrome = substring.lower() == substring.lower()[::-1]
            if is_palindrome:
                set_of_palindromes.add(substring)
    return set_of_palindromes
