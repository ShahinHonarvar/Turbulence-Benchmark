
def palindromes_of_specific_lengths(string):
    # Define the substring range for palindromes
    substr_range = range(106, 281)
    # Initialize an empty set to store palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(len(string)):
        # Get the substring starting at index i and ending at the end of the string
        substr = string[i:]
        # Check if the substring is a palindrome within the specified range
        if substr in substr_range:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
