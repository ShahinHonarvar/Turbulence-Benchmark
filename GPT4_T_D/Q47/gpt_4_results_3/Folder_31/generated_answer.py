
import re

def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    letters_only = re.sub('[^a-z]', '', s)
    palindromes = set()

    for length in range(37, 61):
        for i in range(len(letters_only) - length + 1):
            substring = letters_only[i:i+length]
            
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
