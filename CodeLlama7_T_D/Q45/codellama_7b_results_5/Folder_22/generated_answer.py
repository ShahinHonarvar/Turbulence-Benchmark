
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(5, len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the index of the current character in the alphabet
            index = ord(string[i]) - ord('a')
            # Create a palindrome by reversing the characters in the range [5, i]
            palindrome = ''.join(reversed(string[5:i+1]))
            # Add the palindrome to the set if it has length of at least 3 and all its letters occur between index 5 and index 6
            if len(palindrome) >= 3 and all(letter in range(index, index + 2) for letter in palindrome)):
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
