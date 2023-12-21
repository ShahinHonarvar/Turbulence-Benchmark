
def palindromes_between_indices(string):
    # Create a list of all possible substrings of length at least 3
    substrings = [string[i:j+1] for i in range(len(string)-2) for j in range(i+2, len(string))]
    # Filter the substrings to only include palindromes
    palindromes = []
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
