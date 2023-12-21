
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over the characters of the string
    for i in range(127, 289):
        # Check if the substring from index i-118 to i+140 is a palindrome
        if string[i-118:i+140] == string[i-118:i+140][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(string[i-118:i+140])
    
    # Return the set of palindromes
    return palindromes
