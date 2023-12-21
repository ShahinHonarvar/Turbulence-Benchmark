 def palindromes_of_specific_lengths(string):
    # Define the range of lengths for which we are looking for palindromes
    lengths = range(136, 160 + 1)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the range and find palindromes of that length
    for length in lengths:
        # Find the starting index of the first character of the current length
        start_index = 100 - (length // 2)
        # Find the ending index of the last character of the current length
        end_index = 295 + (length // 2)
        # Iterate over each position in the range and check if it is a palindrome
        for i in range(start_index, end_index + 1):
            # Check if the string starting at index i is a palindrome
            if string[i:] == string[i:][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:])
    return palindromes
