
def palindrome_of_length_at_least_n(s):
    s = ''.join(c.lower() for c in s if c.isalpha())
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i+16, length+1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
