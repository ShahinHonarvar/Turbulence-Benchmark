
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at position i
        char = string[i]
        # Check if the character is a letter (uppercase or lowercase)
        if char.isalpha():
            # Convert the character to uppercase
            char_upper = char.upper()
            # Loop through each character in the reversed substring starting at position i
            for j in range(i, len(string)):
                # Get the character at position j
                rev_char = string[j]
                # Check if the character is a letter (uppercase or lowercase)
                if rev_char.isalpha():
                    # Convert the character to uppercase
                    rev_char_upper = rev_char.upper()
                    # If the converted characters are equal and have a length greater than or equal to n, add them to the palindromes set
                    if char_upper == rev_char_upper and len(char_upper + rev_char_upper) >= n:
                        palindromes.add(char_upper + rev_char_upper)
    # Return the palindromes set
    return palindromes
