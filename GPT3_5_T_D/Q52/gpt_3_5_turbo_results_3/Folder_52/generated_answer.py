
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 422):
        substring = string[i:i+423]
        substring = substring.lower()
        if substring == substring[::-1] and all(c.isalpha() for c in substring):
            palindromes.add(substring)
    return palindromes
