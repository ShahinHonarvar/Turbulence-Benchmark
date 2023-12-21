
def palindromes_of_specific_lengths(string, index_range=(26, 90), lengths=(27, 58)):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string within the specified index range
    for i in range(index_range[0], index_range[1] + 1):
        # Calculate the length of the substring starting at index i and ending at index (i + lengths - 1)
        substr_len = lengths[1] - lengths[0] + 1
        # Check if the substring is a palindrome in a case-insensitive manner
        if string[i:i+substr_len].lower() == string[i:i+substr_len][::-1].lower():
            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:i+substr_len])
    # Return the set of palindromes
    return palindromes
