
def palindromes_of_specific_lengths(s):
    def is_palindrome(s):
        return s == s[::-1]
    
    s = s[36:93]
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''.join(c for c in s if c in valid_chars)
    
    palindromes = set()
    for start in range(len(s)):
        for end in range(start+10, min(start+36, len(s)+1)):
            substring = s[start:end]
            if len(substring)>35:
                break
            if is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes
