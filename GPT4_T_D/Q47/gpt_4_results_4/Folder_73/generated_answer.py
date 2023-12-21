
def palindromes_of_specific_lengths(s):
    import re
    s = s[21:63].lower()
    s = re.sub('[^a-z]', '', s)
    n = len(s)
    palindrome_set = set()

    for length in range(22, 34):
        for i in range(n-length+1):
            substring = s[i : i+length]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
