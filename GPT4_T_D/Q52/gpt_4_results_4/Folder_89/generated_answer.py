
def palindrome_of_length_n(s):
    s = s.lower()
    n = 37
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and all(char.isalpha() for char in sub):
                palindromes.add(sub)
    return palindromes
