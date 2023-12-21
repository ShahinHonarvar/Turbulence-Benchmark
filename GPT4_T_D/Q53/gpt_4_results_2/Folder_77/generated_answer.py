
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s.lower() if c.isalpha())
    length = len(s)
    palindromes = set()

    for i in range(length):
        for j in range(i + 149, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
                
    return palindromes
