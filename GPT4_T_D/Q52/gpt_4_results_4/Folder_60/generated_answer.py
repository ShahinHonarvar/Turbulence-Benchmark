
def palindrome_of_length_n(s):
    s_lower = s.lower()
    palindromes = set()
    for i in range(len(s) - 88 + 1):
        substring = s_lower[i:i+88]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(s[i:i+88])
    return palindromes
