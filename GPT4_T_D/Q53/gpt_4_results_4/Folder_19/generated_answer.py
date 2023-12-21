
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s.lower() if c.isalpha())
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 23, length + 1):
            sub_string = s[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes
