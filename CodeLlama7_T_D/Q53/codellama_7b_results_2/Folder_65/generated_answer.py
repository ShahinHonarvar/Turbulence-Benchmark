
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at position i
        char = string[i]
        # Check if the character is a letter (a-zA-Z)
        if char.isalpha():
            # Convert the character to lowercase
            char = char.lower()
            # Reverse the character
            rev_char = char[::-1]
            # Check if the reversed character is equal to the original character
            if char == rev_char:
                # If the condition is true, add the character to the set of palindromes
                palindromes.add(char)
    # Return the set of palindromes
    return palindromes
