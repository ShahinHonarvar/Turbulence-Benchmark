
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^a-z]', '', s.lower())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 95, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
