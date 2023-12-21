
def palindromes_of_specific_lengths(string):
    # Define the range of lengths that should be considered
    length_range = range(10, 21)
    # Define the range of indices that should be considered
    index_range = range(10, 76)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the length range
    for length in length_range:
        # Get the substring that corresponds to the current length
        substring = string[index_range[0]:index_range[-1]]
        # Iterate over each index in the substring
        for i in range(len(substring)):
            # Get the slice of the substring that starts at the current index and has a length equal to the current length
            slice_ = substring[i:i+length]
            # Check if the slice is a palindrome
            if slice_ == slice_[::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(slice_)
    # Return the set of palindromes
    return palindromes
