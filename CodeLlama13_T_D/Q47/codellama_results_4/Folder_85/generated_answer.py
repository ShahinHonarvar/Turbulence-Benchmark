
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate through each substring of length 6-9 in the specified index range
    for i in range(29, 98 + 1):
        for j in range(i, min(i + 7, len(string)) + 1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])

    # Return the set of all palindromes found
    return palindromes
