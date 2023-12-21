
def palindromes_of_specific_lengths(string):
    indices = range(16, 78)
    lengths = range(43, 48)
    palindromes = set()
    for i in indices:
        for j in lengths:
            substring = string[i:i+j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
