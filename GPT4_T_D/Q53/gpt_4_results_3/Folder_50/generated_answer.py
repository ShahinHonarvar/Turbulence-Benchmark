
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    length = len(s)
    palindrome_set = set()

    for i in range(length):
        for j in range(i + 91, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)

    return palindrome_set
