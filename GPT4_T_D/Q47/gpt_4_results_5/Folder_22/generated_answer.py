
import re

def palindromes_of_specific_lengths(s):
    substr = s[100:201].lower()
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i+5, min(i+11, len(substr)+1)):
            possible_palindrome = substr[i:j]
            if re.match('^[a-z]*$', possible_palindrome) and possible_palindrome == possible_palindrome[::-1]:
                palindromes.add(possible_palindrome)
    return palindromes
