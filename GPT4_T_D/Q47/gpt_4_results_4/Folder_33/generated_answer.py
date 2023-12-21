
def palindromes_of_specific_lengths(s):
    import re
    s = s[130:296]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 103, min(i + 159, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr.lower())
    return palindromes
