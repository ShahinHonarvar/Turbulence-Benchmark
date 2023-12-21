 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the current character and its index
        char = string[i]
        idx = i

        # Check if the character is a letter (lowercase or uppercase)
        if (char.isalpha()):
            # Convert the character to lowercase for case-insensitive comparison
            lower_char = char.lower()

            # Loop through each character in the string starting from the current index and moving towards the end of the string
            for j in range(idx+1, len(string)):
                # Get the next character after the current index
                next_char = string[j]

                # Check if the next character is a letter (lowercase or uppercase)
                if (next_char.isalpha()):
                    # Convert the next character to lowercase for case-insensitive comparison
                    lower_next_char = next_char.lower()

                    # Check if the current character is equal to the next character in a case-insensitive manner
                    if (lower_char == lower_next_char):
                        # Get the length of the palindrome starting from the current index and ending at the next index
                        length = j - idx + 1

                        # Check if the length is greater than or equal to 3
                        if (length >= 3):
                            # Add the palindrome to the set of palindromes
                            palindromes.add(string[idx:j+1])

    # Return the set of palindromes
    return palindromes
