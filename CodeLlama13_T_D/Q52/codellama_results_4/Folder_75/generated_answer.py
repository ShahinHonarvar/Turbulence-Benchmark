
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        substring = string[i:i+80]
        if len(substring) == 80 and all(c.isalpha() for c in substring):
            reverse_substring = substring[::-1]
            if substring == reverse_substring:
                palindromes.add(substring)
    return palindromes
