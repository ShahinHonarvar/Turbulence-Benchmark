
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 23, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindrome_set.add(substr)
    return palindrome_set
