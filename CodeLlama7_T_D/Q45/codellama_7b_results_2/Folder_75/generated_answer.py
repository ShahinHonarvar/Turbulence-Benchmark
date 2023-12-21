 def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome between indices 2 and 4 (inclusive)
    for length in range(3, len(input_string) - 1):
        # Generate all possible combinations of letters between indices 2 and 4 (inclusive)
        for combination in itertools.combinations(input_string[2:5], length):
            # Check if the current combination is a palindrome
            if ''.join(reversed(combination)) == ''.join(combination):
                # Add the current palindrome to the set of palindromes
                palindromes.add(''.join(combination))
    # Return the set of palindromes
    return palindromes
