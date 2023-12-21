
def palindrome_of_length_n(s):
    palindromes = set()
    n = 100
    s = s.lower()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
