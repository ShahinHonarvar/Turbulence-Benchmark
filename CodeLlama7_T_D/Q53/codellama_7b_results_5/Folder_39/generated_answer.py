
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter (not a space or other non-letter character)
        if char.isalpha():
            # Loop through each character in the reversed substring starting at index i
            for j in range(len(string)-i)):
                # Get the character at index j
                rev_char = string[j]
                # If the character is a letter (not a space or other non-letter character)
                if rev_char.isalpha():
                    # Check if the character and its reverse are the same
                    if char == rev_char:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(string[i:j+1])
    # Return the set of palindromes
    return palindromes
