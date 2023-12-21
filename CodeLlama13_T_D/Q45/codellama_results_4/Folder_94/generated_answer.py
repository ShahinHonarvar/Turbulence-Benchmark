
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of the English letters in the given string that occur between index 3 to index 4, both inclusive
    for i in range(3, len(string) - 2):
        # Check if the substring from index 3 to index 4 is a palindrome
        if string[i] == string[len(string) - i - 1]:
            # Add the palindrome to the set
            palindromes.add(string[i:len(string) - i])
    
    # Return the set of all palindromes of the length of at least 3
    return palindromes
