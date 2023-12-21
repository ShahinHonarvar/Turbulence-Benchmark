
def palindromes_of_specific_lengths(string):
    # Lowercase the string for case-insensitive matching
    string = string.lower()
    # Define the range of indices to search in the string
    start_index = 10
    end_index = 70
    # Initialize an empty set to store the palindromes found
    palindromes = set()
    # Iterate over the characters in the string within the specified range
    for i in range(start_index, end_index + 1):
        # Check if the substring starting at index i is a palindrome of length between 24 and 52 (both inclusive)
        substr = string[i:i+23]
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes found
            palindromes.add(substr)
    # Return the set of palindromes found within the specified range
    return palindromes
