
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome between indices 0 and 5
    for length in range(3, len(string) + 1):
        # Generate all combinations of letters between indices 0 and 5
        combinations = itertools.combinations(string, length)
        # Check if each combination is a palindrome
        for combination in combinations:
            if combination == combination[::-1]:
                palindromes.add("".join(combination))
    return palindromes
