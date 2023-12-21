
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each possible combination of 4 letters between indices 3 and 7
    for i in range(3, 8):
        for j in range(i + 1, 9):
            # Extract the substring between indices i and j
            substr = string[i:j]
            
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
