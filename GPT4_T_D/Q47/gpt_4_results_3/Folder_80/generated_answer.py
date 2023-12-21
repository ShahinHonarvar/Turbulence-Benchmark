
def palindromes_of_specific_lengths(string):
    import re
    string = string[35:89]
    palindromes = set()
    for i in range(24, 34):
        for j in range(len(string) - i + 1):
            substr = string[j:j+i]
            if substr == substr[::-1] and re.match("^[A-Za-z]*$", substr):
                palindromes.add(substr.lower())
    return palindromes
