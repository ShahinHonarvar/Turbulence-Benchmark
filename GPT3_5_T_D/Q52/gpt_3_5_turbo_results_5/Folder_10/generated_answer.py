
def palindrome_of_length_n(s):
    n = 54
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
