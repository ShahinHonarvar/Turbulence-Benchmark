
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, len(string)):
        # Check if the substring starting at index 3 and ending at index i-1 is a palindrome
        if string[i - 2] == string[i - 1]:
            # Add the palindrome to the set
            palindromes.add(string[i - 2] + string[i - 1] + string[i])
    # Return the set of palindromes
    return palindromes
