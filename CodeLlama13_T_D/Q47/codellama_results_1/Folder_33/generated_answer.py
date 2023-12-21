
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each substring of length 103 to 158 (both inclusive) in the given string
    for i in range(103, 159):
        # Get the substring from index 130 to index 295 (both inclusive)
        substring = string[130:296]

        # Loop through each palindrome of length i in the given substring
        for j in range(len(substring)):
            # Check if the palindrome is a valid palindrome
            if substring[j:j+i] == substring[j+i-1::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(substring[j:j+i])
    
    # Return the set of palindromes
    return palindromes
