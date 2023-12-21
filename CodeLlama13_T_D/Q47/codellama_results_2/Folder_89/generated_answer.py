
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring from index 18 to index 88, both inclusive
    for i in range(18, 89):
        # Check if the length of the substring is between 12 and 14 (both inclusive)
        if len(string[i:i+15]) in range(12, 15):
            # Check if the substring is a palindrome
            if string[i:i+15] == string[i:i+15][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:i+15])
    
    # Return the set of palindromes
    return palindromes
