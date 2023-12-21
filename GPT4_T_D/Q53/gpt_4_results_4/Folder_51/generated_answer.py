
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindrome_set = set()

    for start in range(len(s)):
        for length in range(3, len(s) - start + 1):
            substring = s[start:start+length]
            if length >= 63 and substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)

    return palindrome_set
