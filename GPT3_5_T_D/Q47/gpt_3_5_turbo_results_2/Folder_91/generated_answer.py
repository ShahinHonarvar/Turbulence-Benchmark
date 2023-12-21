
import string

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11):
        for j in range(i + 3, min(i + 6, 11)):
            substring = s[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
