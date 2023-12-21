
def palindromes_of_specific_lengths(string):
    lengths = range(3, 6)
    indices = range(0, 6)
    palindromes = set()
    for length in lengths:
        for index in indices:
            substr = string[index:index + length]
            if len(substr) != length:
                continue
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
