
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 318, len(s) + 1):
            substring = s[i:j]
            if all(char.isalpha() for char in substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
