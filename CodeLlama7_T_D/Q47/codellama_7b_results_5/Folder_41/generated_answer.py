 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length between 3 and 4 in the given string
    for i in range(1, len(string) - 2):
        # Check if the current substring is a palindrome
        if string[i:i+2] == string[i:i+2][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:i+2])
    # Return the set of palindromes found in the given string
    return palindromes
