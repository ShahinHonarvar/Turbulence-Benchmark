
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(23, 95):
        # Check if the substring starting at index i is a palindrome
        if string[i:] == string[i:][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:])
    # Return the set of palindromes that meet the specified criteria
    return palindromes
