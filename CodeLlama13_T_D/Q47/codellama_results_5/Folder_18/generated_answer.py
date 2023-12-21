
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring from index 11 to index 83, both inclusive
    for i in range(11, 84):
        # Check if the length of the substring is between 13 and 66 (both inclusive)
        if len(string[i:]) >= 13 and len(string[i:]) <= 66:
            # Check if the substring is a palindrome
            if string[i:] == string[i:][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:])
    
    # Return the set of palindromes
    return palindromes
