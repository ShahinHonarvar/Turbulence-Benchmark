
def palindromes_of_specific_lengths(string):
    # Define the range of lengths for palindromes
    length_range = range(34, 55)
    # Define the range of indices for the substring
    index_range = range(11, 94)
    # Create an empty set to store the palindromes
    palindromes = set()
    # Loop through each length in the length_range
    for length in length_range:
        # Calculate the number of palindromes with the current length
        num_palindromes = (len(string) - length + 1) * 2
        # Loop through each index in the index_range
        for index in index_range:
            # Check if there is a palindrome at the current index
            if string[index:index+length] == string[index:index+length][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[index:index+length])
    # Return the set of palindromes
    return palindromes
