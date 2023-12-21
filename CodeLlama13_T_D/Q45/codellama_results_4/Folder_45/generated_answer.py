
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length 4 or more in the given string that occurs between indices 5 and 9, both inclusive
    for i in range(5, 10):
        for j in range(i + 3, len(string)):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)

    # Return the set of all palindromes found
    return palindromes
