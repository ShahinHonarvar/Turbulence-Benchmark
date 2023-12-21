
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^A-Za-z]', '', s).lower()
    n = 46
    palindromes = set()

    for i in range(len(s) - n + 1):
        for j in range(i + n - 1, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                palindromes.add(substring)
                
    return palindromes
