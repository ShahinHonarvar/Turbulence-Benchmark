
def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    length_range = range(100, 170)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the range
    for length in length_range:
        # Define the starting and ending indices for the substring
        start_index = 103
        end_index = 276
        # Iterate over each character in the substring
        for i in range(start_index, end_index):
            # Check if the current character is a palindrome
            if string[i:i+length] == string[i:i+length][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:i+length])
    return palindromes
