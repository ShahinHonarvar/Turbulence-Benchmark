
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(6, 10):
        # Check if the character is a letter or not
        if string[i].isalpha():
            # Get the lowercase version of the character
            char_lower = string[i].lower()
            # Create a palindrome by concatenating the character with its reverse
            palindrome = char_lower + char_lower[::-1]
            # Add the palindrome to the set
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
