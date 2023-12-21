
def palindromes_of_specific_lengths(string):
    indices = range(15, 73)
    lengths = range(19, 56)
    palindromes = set()
    for index in indices:
        for length in lengths:
            substr = string[index : index + length]
            if len(substr) < length:
                break
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
