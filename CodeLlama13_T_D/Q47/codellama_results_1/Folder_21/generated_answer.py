
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Loop through each substring of length 136 to 160 (both inclusive) in the specified index range
    for i in range(100, 295):
        for j in range(i + 136, i + 160 + 1):
            # Check if the substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
