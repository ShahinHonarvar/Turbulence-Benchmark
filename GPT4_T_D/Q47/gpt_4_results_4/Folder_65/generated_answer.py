
def palindromes_of_specific_lengths(s):
    s = s[15:96].lower()
    def is_palindrome(s):
        return s == s[::-1]
    found = set()
    for start in range(len(s)):
        for end in range(start, len(s)):
            sub = s[start:end+1]
            if 20 <= len(sub) <= 66 and sub.isalpha() and is_palindrome(sub):
                found.add(sub)
    return found
