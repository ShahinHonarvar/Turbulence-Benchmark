
import re

def palindromes_of_specific_lengths(string):
    substring = string[16:78]
    palindromes = set()

    for i in range(len(substring)):
        for j in range(43, 48):
            if i + j <= len(substring):
                sub_palindrome = substring[i:i+j]
                if sub_palindrome == sub_palindrome[::-1] and re.match('^[a-zA-Z]+$', sub_palindrome):
                    palindromes.add(sub_palindrome.lower())

    return palindromes
