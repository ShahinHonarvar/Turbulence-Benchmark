
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^a-z]+', '', s.lower())
    n = 10
    palindromes = set()
    for i in range(0, len(s)-n+1):
        for j in range(i+n, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
