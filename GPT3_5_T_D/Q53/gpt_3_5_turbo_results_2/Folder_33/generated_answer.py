
import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = re.sub(r'[^a-zA-Z]', '', s)
    n = len(s)

    for i in range(n - 140):
        for j in range(i + 141, n + 1):
            substring = s[i:j]
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)

    return palindromes
