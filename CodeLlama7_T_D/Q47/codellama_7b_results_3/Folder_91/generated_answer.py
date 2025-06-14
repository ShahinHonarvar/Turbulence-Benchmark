
def palindromes_of_specific_lengths(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Define a set to store all palindromes of lengths between 3 and 5
    palindromes = set()

    # Iterate through the substring from index 0 to index 10, both inclusive
    for i in range(10):
        # Get the current character at index i
        char = string[i]

        # Check if the current character is a letter
        if char.isalpha():
            # Get the corresponding uppercase letter
            upper_char = char.upper()

            # Check if the current character is a vowel (a, e, i, o, u)
            if upper_char in ['A', 'E', 'I', 'O', 'U']:
                # Get the next character at index i + 1
                next_char = string[i + 1]

                # Check if the next character is a letter
                if next_char.isalpha():
                    # Get the corresponding uppercase letter
                    next_upper_char = next_char.upper()

                    # Check if the current and next characters form a palindrome of length 3 to 5
                    if (upper_char + next_upper_char) == (next_upper_char + upper_char):
                        # Add the palindrome to the set of all palindromes found in the substring
                        palindromes.add(upper_char + next_upper_char)

    # Return the set of all palindromes found in the substring from index 0 to index 10, both inclusive
    return palindromes
