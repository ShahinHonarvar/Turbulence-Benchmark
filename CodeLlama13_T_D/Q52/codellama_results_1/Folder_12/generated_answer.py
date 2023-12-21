
def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 23 + 1):
        substring = s[i:i+23]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
