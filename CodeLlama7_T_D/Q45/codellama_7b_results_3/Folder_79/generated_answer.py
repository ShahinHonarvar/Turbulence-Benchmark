
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(1, len(string)):
        # Check if the current character is a palindrome
        if string[i] == string[i:]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i])
    return palindromes
