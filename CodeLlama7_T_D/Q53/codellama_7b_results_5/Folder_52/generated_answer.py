 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # Check if the character is a letter (uppercase or lowercase)
        if char.isalpha():
            # Convert the character to uppercase
            char_upper = char.upper()
            # Loop through each character in the reversed string
            for j in range(len(string)-1, -1, -1):
                # Get the character at index j
                rev_char = string[j]
                # Check if the character is a letter (uppercase or lowercase)
                if rev_char.isalpha():
                    # Convert the character to uppercase
                    rev_char_upper = rev_char.upper()
                    # Check if the character at index i is equal to the character at index j, converted to uppercase
                    if char_upper == rev_char_upper:
                        # If the length of the palindrome is greater than or equal to n, add it to the set of palindromes
                        if len(string[i:j+1]) >= n:
                            palindromes.add(string[i:j+1])
    # Return the set of palindromes
    return palindromes
