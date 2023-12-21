
def palindromes_of_specific_lengths(string):
    # Find all palindromes with the specified length range
    lengths = range(23, 39)
    palindromes = set()
    for length in lengths:
        for i in range(41, 90):
            substring = string[i:i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
