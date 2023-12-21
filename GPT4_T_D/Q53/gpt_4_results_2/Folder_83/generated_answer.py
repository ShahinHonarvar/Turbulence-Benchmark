
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^A-Za-z]', '', s.lower())
    palindrome_set = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 60, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
