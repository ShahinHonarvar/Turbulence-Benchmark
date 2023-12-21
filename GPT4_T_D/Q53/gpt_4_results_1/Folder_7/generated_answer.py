
def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = ''.join(c for c in s if c.isalpha()).lower()
    length_s = len(s)
    if length_s >= 122:
        for i in range(length_s):
            for j in range(i + 122, length_s + 1):
                if s[i:j] == s[i:j][::-1]:
                    palindromes.add(s[i:j])
    return palindromes
