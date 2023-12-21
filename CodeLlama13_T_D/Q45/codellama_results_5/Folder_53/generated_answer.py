
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each possible arrangement of letters in the string
    for i in range(4, 9):
        for j in range(i + 1, len(string)):
            # Check if the substring between indices i and j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
