
def palindrome_of_length_n(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalpha())
    palindromes = set()
    for i in range(len(s) - 18 + 1):
        substring = s[i:i+18]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
