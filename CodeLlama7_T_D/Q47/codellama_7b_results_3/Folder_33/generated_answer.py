
def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    min_length = 103
    max_length = 158
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(len(string) - max_length + 1):
        # Check if the substring starting at index i has a length within the specified range
        if min_length <= len(string[i:]) <= max_length:
            # Check if the substring is a palindrome
            if string[i:] == string[i:][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:])
    # Return the set of palindromes found in the specified index range
    return palindromes
