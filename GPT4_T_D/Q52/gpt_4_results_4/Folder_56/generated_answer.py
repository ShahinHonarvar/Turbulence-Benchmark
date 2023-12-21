
def palindrome_of_length_n(s):
    s = s.lower()
    length = 95
    palindromes = set()
    for i in range(len(s)):
        if i+length <= len(s):
            substring = s[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
