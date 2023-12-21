
def palindrome_of_length_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    palindromes = set()
    for i in range(len(s) - 205):
        substring = s[i:i+206]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
