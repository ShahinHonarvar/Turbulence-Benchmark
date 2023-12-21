
def palindromes_of_specific_lengths(string, index_range=(41, 89), lengths=(23, 38)):
    # Convert string to lowercase
    string = string.lower()
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each index in the range
    for i in range(*index_range):
        # Check if the substring starting at index i is a palindrome
        if string[i:].lower() == string[i:].lower()[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:])
    # Return the set of palindromes that meet the specified criteria
    return palindromes
