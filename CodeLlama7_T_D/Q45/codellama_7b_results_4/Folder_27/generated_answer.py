
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the given string
    for i in range(2, len(string) - 8 + 1):
        # Check if the substring starting at index i and ending at index i+8 is a palindrome
        if string[i:i+8] == string[i:i+8][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+8])
    # Return the set of palindromes
    return palindromes
