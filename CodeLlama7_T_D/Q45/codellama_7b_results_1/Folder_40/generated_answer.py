 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the string
    for i in range(4, 9 + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a copy of the original string
            copy = string[:]
            # Replace the current character with its uppercase equivalent
            copy = copy.replace(string[i], string[i].upper())
            # Check if the modified string is a palindrome
            if copy == copy[::-1]:
                # Add the palindrome to the set
                palindromes.add(copy)
    # Return the set of palindromes
    return palindromes
