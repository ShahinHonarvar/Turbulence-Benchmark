
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the given string between indices 2 and 8, both inclusive
    for i in range(2, 9):
        for j in range(i + 1, 9):
            # Extract the substring from indices i to j
            substr = string[i:j]
            
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    
    # Return the set of all palindromes found
    return palindromes
