
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(16, 40):
        for i in range(16, 61 - length):
            substring = string[i:i+length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
