
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the possible starting indices of a 6-letter palindrome in the given string
    for i in range(3, len(string) - 2):
        # Check if the substring starting at index i and ending at index i + 5 forms a palindrome
        if string[i:i + 5] == string[i:i + 5][::-1]:
            # If it does, add it to the set of palindromes
            palindromes.add(string[i:i + 5])
    # Return the set of palindromes
    return palindromes
