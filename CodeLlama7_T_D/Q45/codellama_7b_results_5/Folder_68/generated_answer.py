
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible arrangement of the English letters in the given string that occur between index 1 and index 8, both inclusive
    for i in range(1, len(string) - 2):
        # Check if the substring starting at index i and ending at index i + 4 is a palindrome
        if string[i:i + 4] == string[i:i + 4][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i + 4])
    # Return the set of palindromes
    return palindromes
