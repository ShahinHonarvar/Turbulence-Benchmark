
def palindrome_of_length_n(s):
    s = s.lower()
    n = 18
    palindromes = set()
    for i in range(0, len(s) - n + 1):
        substring = s[i:i+n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
