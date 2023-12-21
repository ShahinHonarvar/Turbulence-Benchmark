
def palindromes_of_specific_lengths(s):
    import re
    s = s[26:91].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 27, min(i + 59, len(s) + 1)):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
