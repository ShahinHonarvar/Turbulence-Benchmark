
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 10, length + 1):
            segment = s[i:j]
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes
