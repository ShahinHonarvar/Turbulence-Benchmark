
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+56, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and all(ch.isalpha() for ch in substring):
                palindromes.add(substring)
    return palindromes
