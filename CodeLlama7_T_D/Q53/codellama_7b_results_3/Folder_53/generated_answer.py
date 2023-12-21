 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (a-zA-Z)
        if string[i].isalpha():
            # Convert the character to uppercase
            char = string[i].upper()
            # Loop through each character in the string from the current index to the end of the string
            for j in range(i + 1, len(string) + 1):
                # Check if the character is a letter (a-zA-Z)
                if string[j].isalpha():
                    # Convert the character to uppercase
                    other_char = string[j].upper()
                    # Check if the two characters are the same and they are not at the beginning or end of the palindrome
                    if char == other_char and (i > 0 and j < len(string) - 1):
                        # Add the palindrome to the set
                        palindromes.add(char + other_char + char)
    # Return the set of palindromes
    return palindromes
