
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(s)):
        # Get the character at index i
        char = s[i]
        # If the character is not a letter, skip it
        if not char.isalpha():
            continue

        # Loop through each character in the string from index 2 to index 4 (inclusive)
        for j in range(2, min(len(s), 4)):
            # Get the character at index j
            other_char = s[j]
            # If the character is not a letter, skip it
            if not other_char.isalpha():
                continue

            # Check if the two characters are the same (case-insensitive)
            if char.lower() == other_char.lower():
                # Add the palindrome to the set of palindromes
                palindromes.add(char + other_char + char)
    # Return the set of palindromes
    return palindromes
