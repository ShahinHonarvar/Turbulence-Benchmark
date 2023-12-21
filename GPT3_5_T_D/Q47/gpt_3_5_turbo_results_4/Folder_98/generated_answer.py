
def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string[:21].lower()
    for length in range(5, 81):
        for start in range(0, len(string) - length + 1):
            substring = string[start : start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
