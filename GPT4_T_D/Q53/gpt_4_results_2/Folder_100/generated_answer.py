
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 48, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes
