
def palindromes_of_specific_lengths(string):
    # Define the substring of interest
    substr = string[12:122]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(substr)):
        # Get the character and its reverse
        char = substr[i]
        rev_char = substr[i][::-1]
        # If the character is the same as its reverse, add it to the set of palindromes
        if char == rev_char:
            palindromes.add(char)
    # Return the set of palindromes
    return palindromes
