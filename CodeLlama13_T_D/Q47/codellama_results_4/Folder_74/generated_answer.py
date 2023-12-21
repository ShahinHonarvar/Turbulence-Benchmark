
def palindromes_of_specific_lengths(string):
    substr = string[30:84]
    palindromes = set()
    for length in range(12, 21):
        for i in range(len(substr) - length + 1):
            if substr[i : i + length].lower() == substr[i + length - 1 :: -1]:
                palindromes.add(substr[i : i + length])
    return palindromes
