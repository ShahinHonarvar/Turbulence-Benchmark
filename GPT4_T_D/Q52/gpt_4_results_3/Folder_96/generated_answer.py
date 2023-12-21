
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 83 + 1):
        substring = s[i:i+83]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
