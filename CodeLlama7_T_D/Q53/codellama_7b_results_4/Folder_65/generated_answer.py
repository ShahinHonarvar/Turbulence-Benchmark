
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter...
        if char.isalpha():
            # ...loop through each character in the remainder of the string
            for j in range(i + 1, len(string)):
                # Get the character at index j
                other_char = string[j]
                # If the character is a letter...
                if other_char.isalpha():
                    # ...check if the two characters are the same (case-insensitive)
                    if char.lower() == other_char.lower():
                        # If they are, add the palindrome to the set
                        palindromes.add(string[i:j+1])
    # Return the set of palindromes
    return palindromes
