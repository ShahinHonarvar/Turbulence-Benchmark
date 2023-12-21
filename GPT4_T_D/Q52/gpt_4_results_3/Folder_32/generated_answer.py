
def palindrome_of_length_n(s):
    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s)):
        for j in range(i+113, len(s)+1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result
