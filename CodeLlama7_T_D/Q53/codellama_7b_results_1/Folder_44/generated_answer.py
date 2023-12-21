
def palindrome_of_length_at_least_n(string, n=89):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at position i
        char = string[i]
        # If the character is a letter (uppercase or lowercase)
        if char.isalpha():
            # Convert the character to uppercase
            uppercase_char = char.upper()
            # Loop through each character in the string starting from position i + 1
            for j in range(i + 1, len(string)):
                # Get the character at position j
                other_char = string[j]
                # If the character is a letter (uppercase or lowercase)
                if other_char.isalpha():
                    # Convert the character to uppercase
                    uppercase_other_char = other_char.upper()
                    # If the two characters are the same in both cases (i.e., both uppercase and lowercase)
                    if uppercase_char == uppercase_other_char:
                        # Create a palindrome by concatenating the two characters
                        palindrome = char + other_char
                        # If the length of the palindrome is greater than or equal to n, add it to the set of palindromes
                        if len(palindrome) >= n:
                            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
