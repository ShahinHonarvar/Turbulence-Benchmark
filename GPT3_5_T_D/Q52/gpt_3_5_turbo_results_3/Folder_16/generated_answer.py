
def palindrome_of_length_n(s):
    n = 255
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
