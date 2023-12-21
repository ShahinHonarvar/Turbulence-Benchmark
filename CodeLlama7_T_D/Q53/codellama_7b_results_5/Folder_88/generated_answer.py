
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter (lowercase or uppercase)
        if char.isalpha():
            # Convert the character to lowercase
            char_lower = char.lower()
            # Loop through each character in the remaining part of the string
            for j in range(i + 1, len(string)):
                # Get the character at index j
                char2 = string[j]
                # If the character is a letter (lowercase or uppercase)
                if char2.isalpha():
                    # Convert the character to lowercase
                    char2_lower = char2.lower()
                    # Check if the concatenation of the two characters is a palindrome
                    if char_lower + char2_lower == char2_lower + char_lower:
                        # Add the concatenation of the two characters to the set of palindromes
                        palindromes.add(char_lower + char2_lower)
    # Return the set of palindromes
    return palindromes
