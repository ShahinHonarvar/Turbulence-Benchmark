
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalpha())
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 27, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
