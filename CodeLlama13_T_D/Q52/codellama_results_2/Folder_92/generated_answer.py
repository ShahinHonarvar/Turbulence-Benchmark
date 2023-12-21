
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 10 + 1):
        substr = string[i:i+10]
        if len(substr) == 10 and all([char.isalpha() for char in substr]):
            palindromes.add(substr)
    return palindromes
