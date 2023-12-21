
def palindromes_of_specific_lengths(s):
    import re
    s = s[32:80].lower()
    s = re.sub('[^a-z]', '', s)
    palindrome_set = set()
    for l in range(35, 42):
        for i in range(len(s) - l + 1):
            substring = s[i: i + l]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
