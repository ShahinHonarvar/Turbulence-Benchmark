 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter (uppercase or lowercase)
        if char.isalpha():
            # Convert the character to lowercase
            char_lower = char.lower()
            # Check if the character appears in the string more than once
            if string.count(char_lower) > 1:
                # Get the indices of all occurrences of the character in the string
                indices = [i for i, letter in enumerate(string) if letter == char_lower]
                # Loop through each index in the list of indices
                for j in indices:
                    # If the index is greater than or equal to the specified minimum length (n)
                    if j >= n - 1:
                        # Get the substring starting at the index and ending at the end of the string
                        substr = string[j:]
                        # Check if the substring is a palindrome
                        if substr == substr[::-1]:
                            # Add the palindrome to the set of palindromes
                            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
