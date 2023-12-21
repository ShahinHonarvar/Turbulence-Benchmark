
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()

    for i in range(len(s) - 23):
        substring = s[i:i+24]
        if all(char.isalpha() for char in substring) and substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
