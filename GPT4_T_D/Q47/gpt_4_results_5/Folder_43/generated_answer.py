
def palindromes_of_specific_lengths(s):
    import re
    s = s[41:90]
    palindromes = set()
    for i in range(23, 39):
        for j in range(len(s)):
            substring = s[j:j+i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
