
def palindrome_of_length_at_least_n(s):
    s = ''.join(c.lower() for c in s if c.isalpha())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 41, len(s) + 1):
            sub_s = s[i:j]
            if sub_s == sub_s[::-1]:
                palindromes.add(sub_s)
    return palindromes
