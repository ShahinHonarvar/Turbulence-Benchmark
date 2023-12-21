
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if len(substring) == 257 and all(ch.isalpha() for ch in substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    
    return palindromes
