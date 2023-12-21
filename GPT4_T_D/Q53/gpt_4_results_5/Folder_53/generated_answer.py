
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s.lower() if c.isalpha())
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i+64, length+1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
