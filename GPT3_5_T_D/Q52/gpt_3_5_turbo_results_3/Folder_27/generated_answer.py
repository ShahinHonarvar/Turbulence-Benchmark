
def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    n = len(s)
    for i in range(n - 55):
        substring = s[i:i + 56]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
