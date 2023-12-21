
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each letter in the string
    for i in range(len(string)):
        # Get the substring starting from index i and ending at index 2 * i + 1
        substr = string[i:2 * i + 1]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
