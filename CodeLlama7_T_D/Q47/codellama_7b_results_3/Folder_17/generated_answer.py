
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of the specified length in the given string
    for i in range(22, 95 + 1):
        # Get the substring of the specified length starting at index i
        substring = string[i:i + 55]
        # Loop through each palindrome in the substring
        for j in range(len(substring)):
            # Check if the current character is a letter or not
            if (substring[j].isalpha()):
                # Check if the palindrome is of the specified length or not
                if (len(substring) - j >= 52 and len(substring) - j <= 55):
                    # Add the palindrome to the set of palindromes
                    palindromes.add(substring[j:len(substring)]))
    # Return the set of palindromes found in the given string
    return palindromes
