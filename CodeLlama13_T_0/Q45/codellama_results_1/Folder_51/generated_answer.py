
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the given string that occur between indices 3 and 5, both inclusive
    for i in range(3, len(string) - 2):
        for j in range(i + 1, len(string) - 1):
            # Check if the substring from index i to index j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
