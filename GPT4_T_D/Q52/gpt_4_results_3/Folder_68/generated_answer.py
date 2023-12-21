
def palindrome_of_length_n(s):
    s = s.lower()
    all_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 76, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and all(c.isalpha() for c in substring):
                all_palindromes.add(substring)
    return all_palindromes
