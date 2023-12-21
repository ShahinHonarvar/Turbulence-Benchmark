
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring from index 0 to index 6, both inclusive
    for i in range(0, len(string)):
        # Check if the length of the substring is between 3 and 6 (both inclusive)
        if 3 <= len(string[i:]) <= 6:
            # Check if the substring is a palindrome
            if string[i:].lower() == string[i:][::-1].lower():
                # Add the palindrome to the set
                palindromes.add(string[i:])
    
    # Return the set of palindromes
    return palindromes
