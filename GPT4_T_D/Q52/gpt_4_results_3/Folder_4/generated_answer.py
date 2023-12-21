
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+15, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and not any(ch.isdigit() or not ch.isalpha() for ch in substring):
                palindromes.add(substring)
    return palindromes
