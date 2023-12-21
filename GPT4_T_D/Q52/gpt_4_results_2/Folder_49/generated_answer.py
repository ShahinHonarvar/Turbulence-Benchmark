
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        if i + 47 <= len(s):
            substring = s[i:i+47]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
