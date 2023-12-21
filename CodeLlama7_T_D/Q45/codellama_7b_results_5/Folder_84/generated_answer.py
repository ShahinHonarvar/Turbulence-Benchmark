
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the given string
    for i in range(4, 10):
        # Check if the current character is a letter (not a space or punctuation)
        if string[i].isalpha():
            # Create a palindrome by reversing the characters between index 4 and index 9, inclusive
            palindrome = ''.join(reversed(string[4:10]))
            # Add the palindrome to the set of palindromes
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
