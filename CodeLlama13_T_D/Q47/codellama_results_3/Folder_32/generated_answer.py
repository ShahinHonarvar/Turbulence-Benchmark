
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring from index 16 to index 77, both inclusive
    for i in range(16, 78):
        # Check if the substring starting at index i has a length between 43 and 47 (both inclusive)
        if len(string[i:]) >= 43 and len(string[i:]) <= 47:
            # Check if the substring is a palindrome
            if string[i:] == string[i:][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:])
    
    # Return the set of all palindromes found in the specified index range and with the specified lengths
    return palindromes
