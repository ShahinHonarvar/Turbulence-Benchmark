 def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(6, 9):
        # Get the current character and its case-insensitive counterpart
        current_char = input_string[i]
        current_char_lowercase = current_char.lower()
        # Check if the current character is a letter (not a space or any other non-letter character)
        if current_char.isalpha():
            # Get the lowercase version of the current character
            current_char_lowercase = current_char.lower()
            # Loop through each character in the input string from index 6 to index 8, both inclusive
            for j in range(6, 9):
                # Get the current character and its case-insensitive counterpart
                current_char = input_string[j]
                current_char_lowercase = current_char.lower()
                # Check if the current character is a letter (not a space or any other non-letter character)
                if current_char.isalpha():
                    # Get the lowercase version of the current character
                    current_char_lowercase = current_char.lower()
                    # Form the palindrome by concatenating the two characters
                    palindrome = current_char_lowercase + current_char_lowercase[::-1]
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    return palindromes
