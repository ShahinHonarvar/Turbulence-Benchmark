
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 29, len(string) + 1):
            substring = string[i:j]
            clean_substring = ''.join(c for c in substring if c.isalpha())
            if len(clean_substring) == 29 and clean_substring == clean_substring[::-1]:
                palindromes.add(clean_substring)
    return palindromes
