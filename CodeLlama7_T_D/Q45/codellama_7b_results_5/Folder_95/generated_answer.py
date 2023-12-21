
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(7, 9):
        # Check if the character is a letter
        if string[i].isalpha():
            # Get the lowercase version of the character
            lowercase_char = string[i].lower()
            # Add the palindrome to the set
            palindromes.add(lowercase_char + lowercase_char)
    return palindromes
