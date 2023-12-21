
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the character to uppercase
            uppercase_character = string[i].upper()
            # Loop through each character in the remaining part of the string
            for j in range(i + 1, len(string)):
                # Check if the character is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Convert the character to uppercase
                    uppercase_character2 = string[j].upper()
                    # Check if the two characters are equal in a case-insensitive manner
                    if uppercase_character == uppercase_character2:
                        # If they are equal, add the palindrome to the set of palindromes
                        palindromes.add(string[i : j + 1])
    # Return the set of palindromes
    return palindromes
