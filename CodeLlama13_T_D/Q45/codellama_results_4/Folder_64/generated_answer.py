
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of the English letters in the given string that occur between index 4 and index 9, both inclusive
    for i in range(4, 10):
        for j in range(i+1, 10):
            # Check if the substring from i to j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
