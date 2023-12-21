
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter (uppercase or lowercase)
        if char.isalpha():
            # Convert the character to uppercase
            char_upper = char.upper()
            # Loop through each character in the string starting from index i + 1
            for j in range(i + 1, len(string)):
                # Get the character at index j
                other_char = string[j]
                # If the character is a letter (uppercase or lowercase)
                if other_char.isalpha():
                    # Convert the character to uppercase
                    other_char_upper = other_char.upper()
                    # Check if the characters at index i and index j are the same (ignoring case)
                    if char_upper == other_char_upper:
                        # If the length of the substring starting from index i and ending at index j is greater than or equal to n, add it to the set of palindromes
                        if len(string[i:j + 1]) >= n:
                            palindromes.add(string[i:j + 1])
    # Return the set of palindromes in a case-insensitive manner
    return palindromes
