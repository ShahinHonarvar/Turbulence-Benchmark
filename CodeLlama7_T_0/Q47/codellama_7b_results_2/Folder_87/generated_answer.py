
def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    lengths = range(34, 55)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the range
    for length in lengths:
        # Get the substring starting from index 11 and ending at index 93 (both inclusive)
        substring = string[11:94]
        # Iterate over each character in the substring
        for i in range(len(substring)):
            # Check if the current character is a palindrome of length 'length'
            if substring[i:i+length] == substring[i:i+length][::-1]:
                # Add the palindrome to the set
                palindromes.add(substring[i:i+length])
    # Return the set of palindromes found in the specified index range
    return palindromes
