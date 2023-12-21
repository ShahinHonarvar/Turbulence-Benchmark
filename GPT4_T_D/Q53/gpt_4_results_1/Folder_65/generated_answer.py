
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    palindromes = set()
    len_s = len(s)
    for i in range(len_s):
        for j in range(i + 15, len_s + 1):
            sub_s = s[i:j]
            if sub_s == sub_s[::-1]:
                palindromes.add(sub_s)
    return palindromes
