
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub(r'\W+', '', s).lower()
    
    def is_palindrome(s):
        return s == s[::-1]
    
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 115, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
                
    return palindromes
