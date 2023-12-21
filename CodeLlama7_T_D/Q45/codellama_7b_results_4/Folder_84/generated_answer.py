
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, 10):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a palindrome using the current character and its mirror image
            palindrome = string[i] + string[i].lower()
            # Add the palindrome to the set of palindromes
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
