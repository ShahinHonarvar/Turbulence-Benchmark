
def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    lengths = range(37, 61)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the range
    for length in lengths:
        # Get the substring starting from index 11 and ending at index 83 (both inclusive)
        substring = string[11:84]
        # Iterate over each character in the substring
        for i in range(len(substring)):
            # Check if the current character is a palindrome of length 'length'
            if substring[i:] == substring[i:][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(substring[i:])
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
