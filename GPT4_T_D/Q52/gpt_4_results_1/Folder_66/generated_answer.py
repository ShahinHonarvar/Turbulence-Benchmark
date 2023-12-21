
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        if i+25 <= len(s):
            substring = s[i:i+25]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
