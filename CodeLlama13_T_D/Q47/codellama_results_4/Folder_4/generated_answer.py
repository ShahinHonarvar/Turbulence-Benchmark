
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the given string
    palindromes = []
    for i in range(12, 93):
        for j in range(i+17, i+67):
            if j > len(string):
                break
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.append(substr)
    return set(palindromes)
