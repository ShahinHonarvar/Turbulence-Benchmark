 def palindromes_of_specific_lengths(string):
    # Define the substring range and lengths
    start = 28
    end = 94
    lengths = range(38, 50)
    # Create an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the lengths range
    for length in lengths:
        # Get the substring of the specified length
        substr = string[start:end]
        # Check if the substring is a palindrome with the specified length
        if len(substr) == length and substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    return palindromes
