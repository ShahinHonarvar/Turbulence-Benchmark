
import re

def palindromes_of_specific_lengths(s):
    s = s[18:66].lower()
    s = re.sub('[^a-z]', '', s)
    length_s = len(s)
    palindromes = set()

    for i in range(23,37):
        for j in range(0,length_s-i+1):
            potential_palindrome = s[j:j+i]
            if potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)

    return palindromes
