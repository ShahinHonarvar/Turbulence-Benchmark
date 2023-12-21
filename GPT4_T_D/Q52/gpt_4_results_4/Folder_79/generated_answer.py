
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 63):
        substring = s[i:i+64]
        if substring == ''.join(reversed(substring)) and substring.isalpha():
            palindromes.add(substring)
    return palindromes
