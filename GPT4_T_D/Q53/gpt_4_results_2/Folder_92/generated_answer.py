
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    
    for start in range(len(s)):
        for end in range(start + 10, len(s)):
            substring = s[start:end+1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
                
    return palindromes
