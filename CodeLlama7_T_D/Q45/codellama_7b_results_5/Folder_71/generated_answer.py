 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # Check if the character is a letter (uppercase or lowercase)
        if char.isalpha():
            # Convert the character to lowercase
            char = char.lower()
            # Loop through each character in the string from index i + 1 to the end of the string
            for j in range(i + 1, len(string)):
                # Get the character at index j
                other_char = string[j]
                # Check if the character is a letter (uppercase or lowercase)
                if other_char.isalpha():
                    # Convert the character to lowercase
                    other_char = other_char.lower()
                    # If the two characters are the same, add the palindrome formed by these two characters to the set of palindromes
                    if char == other_char:
                        palindromes.add(char + other_char)
    return palindromes
