
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string)):
        # Check if the substring starting at index 2 and ending at index i is a palindrome
        if string[2:i] == string[2:i][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[2:i])
    # Return the set of palindromes
    return palindromes
