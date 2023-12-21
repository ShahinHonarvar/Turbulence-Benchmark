
def palindromes_of_specific_lengths(s):
    import re
    s = s[23:95]
    s = re.sub(r'[^a-z]', '', s.lower())
    palindrome_set = set()
    for i in range(94 - 23 + 1 - 17):
        for j in range(17, min(55, 94 - 23 + 1 - i) + 1):
            substring = s[i:i + j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
