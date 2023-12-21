
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(22, 96):
        for length in range(52, 56):
            substring = string[i:i+length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
