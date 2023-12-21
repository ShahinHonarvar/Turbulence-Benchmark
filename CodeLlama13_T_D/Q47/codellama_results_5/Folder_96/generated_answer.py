
def palindromes_of_specific_lengths(string):
    # Find all palindromes with the specified length in the given string
    palindromes = []
    for i in range(100, 300 + 1):
        for j in range(i, min(i + 100, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.append(string[i:j])
    return set(palindromes)
