
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 400):
        substring = s[i:i+401]
        if not any(c.isalpha() for c in substring):
            continue
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
