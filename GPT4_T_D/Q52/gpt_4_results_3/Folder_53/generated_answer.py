
def palindrome_of_length_n(s):
    import string
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 68 + 1):
        substring = s[i:i+68]
        if all(c in string.ascii_lowercase for c in substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
