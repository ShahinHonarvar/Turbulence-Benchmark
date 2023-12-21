
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the character to uppercase
            char_upper = string[i].upper()
            # Loop through each character in the reversed string
            for j in range(len(string)-1, -1, -1):
                # Check if the character is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Convert the character to uppercase
                    char_upper2 = string[j].upper()
                    # Check if the characters are the same (ignoring case)
                    if char_upper == char_upper2:
                        # Create a tuple of the two characters and add it to the set
                        palindromes.add((char_upper, char_upper2))
            # Loop through each character in the string
            for j in range(len(string)):
                # Check if the character is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Convert the character to uppercase
                    char_upper = string[j].upper()
                    # Check if the characters are the same (ignoring case)
                    if char_upper == char_upper2:
                        # Create a tuple of the two characters and add it to the set
                        palindromes.add((char_upper, char_upper2))
            # Loop through each character in the string
            for j in range(len(string)):
                # Check if the character is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Convert the character to uppercase
                    char_upper = string[j].upper()
                    # Check if the characters are the same (ignoring case)
                    if char_upper == char_upper2:
                        # Create a tuple of the two characters and add it to the set
                        palindromes.add((char_upper, char_upper2))
    # Return the set of all palindromes of length greater than or equal to 81 that exist in the given string
    return palindromes
