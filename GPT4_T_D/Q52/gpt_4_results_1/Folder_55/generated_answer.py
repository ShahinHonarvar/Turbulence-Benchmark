
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    
    for i in range(len(s)):
        for j in range(i + 97, len(s) + 1):
            substring = s[i:j]
            if len(substring) == 97:
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    
    return palindromes
