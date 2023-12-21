
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter
        if char.isalpha():
            # Loop through each character in the remaining substring starting from index i + 1
            for j in range(i + 1, len(string)):
                # Get the character at index j
                other_char = string[j]
                # If the other character is a letter and it is not the same as the current character
                if other_char.isalpha() and other_char != char:
                    # Create a palindrome by concatenating the current character with the other character in reverse order
                    palindrome = char + other_char[::-1]
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
