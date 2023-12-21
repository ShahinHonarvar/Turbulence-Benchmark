
def palindromes_of_specific_lengths(string):
    string = string[23:83]
    palindromes = set()
    for length in range(32, 35):
        for start in range(0, len(string) - length + 1):
            substring = string[start:start + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
