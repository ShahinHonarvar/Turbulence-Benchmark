
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    def is_palindrome(s):
        return s == s[::-1]
    
    s_set = set()
    for i in range(len(s)):
        for j in range(i+59, len(s)+1):
            subset = s[i:j]
            if is_palindrome(subset) and subset.isalpha():
                s_set.add(subset)
    return s_set
