
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each possible arrangement of English letters in the given string that occur between indices 1 and 5, both inclusive
    for i in range(1, 6):
        for j in range(i + 4, len(string)):
            # Check if the substring from index i to index j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
