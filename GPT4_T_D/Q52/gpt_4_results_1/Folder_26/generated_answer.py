
def palindrome_of_length_n(s):
    s = "".join([c.lower() for c in s if c.isalpha()])
    length_s = len(s)
    palindromes = set()
    for i in range(length_s - 365):
        substring = s[i:i+366]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
