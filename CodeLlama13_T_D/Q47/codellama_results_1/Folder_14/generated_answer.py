
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each substring of length 6 to 8
    for i in range(10, 75):
        for j in range(i + 2, i + 9):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
