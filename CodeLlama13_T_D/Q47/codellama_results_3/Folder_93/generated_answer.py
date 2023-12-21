
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring from index 17 to index 95, both inclusive
    for i in range(17, 96):
        # Get the length of the substring
        length = len(string[i:])
        
        # Check if the length is between 13 and 49 (both inclusive)
        if 13 <= length <= 49:
            # Check if the substring is a palindrome
            if string[i:] == string[i:][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:])
    
    return palindromes
