
def palindrome_of_length_at_least_n(string, n=56):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length greater than or equal to 56 in the given string
    for i in range(len(string) - n + 1):
        # Extract the current substring from the main string
        substr = string[i:i+n]

        # Check if the current substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)

    # Return the set of palindromes found in the given string
    return palindromes
