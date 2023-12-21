
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 149, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] :
                palindromes.add(substring)
    return palindromes
