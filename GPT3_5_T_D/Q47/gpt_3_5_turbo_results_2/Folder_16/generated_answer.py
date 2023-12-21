
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:87]
    palindromes = set()

    for length in range(51, 61):
        for start in range(len(substring) - length):
            check_palindrome = substring[start:start + length].lower()
            if re.match("^[a-zA-Z]+$", check_palindrome):
                if check_palindrome == check_palindrome[::-1]:
                    palindromes.add(check_palindrome)

    return palindromes
