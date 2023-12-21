
import re

def palindrome_of_length_n(s):
    palindromes = set()

    s = re.sub('[^a-zA-Z]', '', s.lower())

    for i in range(len(s) - 288):
        substring = s[i:i+289]

        if substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
