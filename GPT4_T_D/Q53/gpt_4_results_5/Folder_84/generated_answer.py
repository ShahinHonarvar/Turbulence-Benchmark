
def palindrome_of_length_at_least_n(s):
    s = "".join(c.lower() for c in s if c.isalpha())
    palindrome_set = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 81, length + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindrome_set.add(substr)
    return palindrome_set
