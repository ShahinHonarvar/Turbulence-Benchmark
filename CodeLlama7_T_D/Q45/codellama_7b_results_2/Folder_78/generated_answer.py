
def palindromes_between_indices(string):
    # Define the indices to check for palindromes
    start_index = 6
    end_index = 8
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the given string within the specified range
    for i in range(start_index, end_index + 1):
        # Check if the character at index 'i' is not a space or an empty string
        if string[i] != " ":
            # Initialize two variables to store the characters on either side of the current character
            left_char = ""
            right_char = ""

            # Iterate over the characters in the given string within the specified range
            for j in range(start_index, end_index + 1):
                # Check if the character at index 'j' is not a space or an empty string
                if string[j] != " ":
                    # If the current character is on the left side of the current character
                    if i == j - 1:
                        # Set the variable 'left_char' to the character at index 'j'
                        left_char = string[j]

                    # If the current character is on the right side of the current character
                    elif i == j + 1:
                        # Set the variable 'right_char' to the character at index 'j'
                        right_char = string[j]

            # Check if both variables 'left_char' and 'right_char' are not empty strings
            if left_char != "" and right_char != "":
                # Initialize a variable to store the palindrome
                palindrome = ""

                # If the current character is on the left side of the current character
                if i == j - 1:
                    # Set the variable 'palindrome' to the concatenation of the characters in the given string within the specified range, with the character at index 'j' being the first character and the character at index 'i' being the last character
                    palindrome = left_char + string[i] + right_char

                # If the current character is on the right side of the current character
                elif i == j + 1:
                    # Set the variable 'palindrome' to the concatenation of the characters in the given string within the specified range, with the character at index 'i' being the first character and the character at index 'j' being the last character
                    palindrome = left_char + right_char + string[i]

                # Check if the variable 'palindrome' is not an empty string
                if palindrome != "":
                    # Add the variable 'palindrome' to the set of palindromes
                    palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
