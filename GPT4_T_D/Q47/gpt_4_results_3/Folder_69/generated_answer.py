
def palindromes_of_specific_lengths(s):
    import re
    s = s[11:97].lower()
    s = re.sub('[^a-z]', '', s)
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 45, min(i + 53, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
