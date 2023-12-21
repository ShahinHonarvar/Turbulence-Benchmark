 def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(input_string)):
        # Get the character at index i
        char = input_string[i]
        # Check if the character is a letter (not a whitespace or a symbol)
        if char.isalpha():
            # Loop through each character in the input string from index i + 1 to the last character
            for j in range(i + 1, len(input_string)):
                # Get the character at index j
                other_char = input_string[j]
                # Check if the character is a letter (not a whitespace or a symbol)
                if other_char.isalpha():
                    # If both characters are letters, check if they form a palindrome of length 7 or more
                    if char.lower() == other_char.lower() and len(input_string[i:j + 1]) >= 7:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(input_string[i:j + 1].lower())
    # Return the set of palindromes
    return palindromes
