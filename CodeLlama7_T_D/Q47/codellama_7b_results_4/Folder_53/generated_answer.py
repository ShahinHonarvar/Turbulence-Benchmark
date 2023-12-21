
def palindromes_of_specific_lengths(string):
    # Define the range of indices for which we want to find palindromes
    indices = range(1, 299)
    # Define the range of lengths for which we want to find palindromes
    lengths = range(3, 10)
    # Initialize an empty set to store the found palindromes
    palindromes = set()
    # Iterate over the indices in the specified range
    for i in indices:
        # Get the substring starting at index i and ending at index (i + length - 1)
        substring = string[i:i + lengths[-1] - 1]
        # Iterate over the lengths in the specified range
        for j in lengths:
            # Get the palindrome of length j from the substring
            palindrome = substring[:j][::-1]
            # Check if the palindrome is found in the substring
            if palindrome in substring:
                # Add the palindrome to the set of found palindromes
                palindromes.add(palindrome)
    return palindromes
