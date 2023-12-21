
def palindromes_between_indices(string, start_index, end_index):
    # Create a set to store all palindromes
    palindromes = set()
    # Iterate over the indices in the specified range
    for i in range(start_index, end_index + 1):
        # Get the character at the current index
        char = string[i]
        # If the character is not a letter, skip to the next index
        if not char.isalpha():
            continue

        # Iterate over the indices in the specified range again
        for j in range(start_index, end_index + 1):
            # Get the character at the current index
            other_char = string[j]
            # If the character is not a letter, skip to the next index
            if not other_char.isalpha():
                continue

            # Create a palindrome by concatenating the two characters
            palindrome = char + other_char

            # Add the palindrome to the set of palindromes
            palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
