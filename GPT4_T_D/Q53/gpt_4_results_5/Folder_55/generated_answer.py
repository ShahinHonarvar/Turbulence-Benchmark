
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    n = 83
    palindromes_set = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes_set.add(sub)
    return palindromes_set
