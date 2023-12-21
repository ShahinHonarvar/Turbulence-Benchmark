
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    n = 9
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
