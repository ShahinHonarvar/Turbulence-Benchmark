
def palindrome_of_length_n(s):
    def is_palindrome(s):
        return s == s[::-1]
    
    s = s.lower()
    result = set()

    for i in range(len(s)):
        for j in range(i + 113, len(s) + 1):
            sub = s[i:j]
            if is_palindrome(sub) and sub.isalpha():
                result.add(sub)
    
    return result
