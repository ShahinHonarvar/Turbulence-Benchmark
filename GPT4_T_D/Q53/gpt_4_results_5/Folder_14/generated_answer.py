
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    results = set()
    
    def is_palindrome(s):
        return s == s[::-1]
    
    for i in range(len(s)):
        for j in range(i+13, len(s)+1):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                results.add(s[i:j])
    
    return results
