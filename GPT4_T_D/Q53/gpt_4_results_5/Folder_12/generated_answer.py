
def palindrome_of_length_at_least_n(s):
    import re
    from collections import Counter
    s = re.sub(r'[^A-Za-z]', '', s.lower())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+51, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
