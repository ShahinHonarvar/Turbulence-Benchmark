
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub(r'\W+', '', s).lower()
    palindromes = set()
    length = len(s)
    for i in range(83, length + 1):
        for j in range(length - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
