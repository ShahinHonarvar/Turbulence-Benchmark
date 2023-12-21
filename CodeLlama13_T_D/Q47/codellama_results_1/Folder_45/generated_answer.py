
def palindromes_of_specific_lengths(string):
    # Convert the string to a set of lowercase characters
    chars = set(string.lower())
    
    # Define the range of lengths to consider (3-60)
    lengths = range(3, 61)
    
    # Define the range of indices to consider (70-140)
    indices = range(70, 141)
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each length in the specified range
    for length in lengths:
        # Iterate over each index in the specified range
        for i in indices:
            # Check if the substring from index i to index i+length-1 is a palindrome
            substr = string[i:i+length]
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    
    return palindromes
