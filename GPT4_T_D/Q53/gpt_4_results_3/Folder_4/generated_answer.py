
def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = ''.join(c for c in s if c.isalpha()).lower()
    length = len(s)
    for i in range(length):
        for j in range(i+99, length+1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
