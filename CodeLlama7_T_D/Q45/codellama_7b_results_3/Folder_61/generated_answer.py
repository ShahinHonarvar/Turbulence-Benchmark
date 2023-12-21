 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # Check if the character is a letter (not a digit or special character)
        if char.isalpha():
            # Convert the character to uppercase
            char_upper = char.upper()
            # Loop through each character in the string starting from index i + 1
            for j in range(i + 1, len(string)):
                # Get the character at index j
                other_char = string[j]
                # Check if the other character is a letter (not a digit or special character)
                if other_char.isalpha():
                    # Convert the other character to uppercase
                    other_char_upper = other_char.upper()
                    # Check if the two characters are the same (ignoring case)
                    if char_upper == other_char_upper:
                        # Get the substring of the string starting from index i and ending at index j
                        substr = string[i:j + 1]
                        # Check if the substring is a palindrome (ignoring case)
                        if substr.lower() == substr[::-1].lower():
                            # Add the palindrome to the set of palindromes
                            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
