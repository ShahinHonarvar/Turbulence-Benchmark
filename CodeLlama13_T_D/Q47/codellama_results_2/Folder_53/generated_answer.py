
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(1, 299):
        for j in range(i+2, min(i+11, len(string))):
            substr = string[i:j]
            if substr == substr[::-1] and all(chr.isalpha() for chr in substr):
                palindromes.add(substr)
    return palindromes
