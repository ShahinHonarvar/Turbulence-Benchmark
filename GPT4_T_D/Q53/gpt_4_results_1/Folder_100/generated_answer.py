
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub(r'\W+', '', s).lower()
    n = 48
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
