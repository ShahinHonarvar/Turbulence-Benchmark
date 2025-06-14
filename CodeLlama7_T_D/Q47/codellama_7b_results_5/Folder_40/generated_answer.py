
def palindromes_of_specific_lengths(string, lengths=range(3, 6)):
    palindromes = set()
    for length in lengths:
        for i in range(len(string) - length + 1):
            substr = string[i:i+length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
