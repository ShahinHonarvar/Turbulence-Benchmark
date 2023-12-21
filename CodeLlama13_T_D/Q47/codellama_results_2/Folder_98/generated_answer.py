
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each substring of length 5 to 80 (both inclusive)
    for i in range(5, 81):
        # Check if the substring is a palindrome
        if string[0:i] == string[0:i][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[0:i])

    # Return the set of palindromes
    return palindromes
