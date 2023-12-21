
def palindromes_between_indices(string):
    # Create a list of all possible substrings
    # of length at least 7 between indices 2 and 9
    substrings = [string[i:j+1] for i in range(2, len(string)-8) for j in range(i+2, len(string)-6)]
    # Filter out substrings that are not palindromes
    palindromes = []
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
