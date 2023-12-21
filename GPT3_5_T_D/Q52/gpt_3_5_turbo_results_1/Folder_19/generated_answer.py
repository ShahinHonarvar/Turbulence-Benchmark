
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 66):
        substring = string[i:i+67]
        lower_substring = substring.lower()
        if lower_substring == lower_substring[::-1] and all(c.isalpha() for c in substring):
            palindromes.add(substring)
    return palindromes
