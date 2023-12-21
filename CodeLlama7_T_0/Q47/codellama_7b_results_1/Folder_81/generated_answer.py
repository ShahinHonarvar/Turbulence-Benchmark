
def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    lengths = range(12, 220 + 1)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the range
    for length in lengths:
        # Get the substring of the specified length from the index range
        substring = string[12:122 + 1][length]]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
