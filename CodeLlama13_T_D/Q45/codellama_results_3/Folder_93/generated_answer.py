
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Loop through each possible arrangement of English letters in the given string that occur between index 2 to index 7, both inclusive
    for i in range(2, len(string) - 6):
        for j in range(i + 1, len(string) - 5):
            # Check if the substring between indices i and j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
