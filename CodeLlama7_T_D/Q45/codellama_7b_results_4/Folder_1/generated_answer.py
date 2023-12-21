 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # Check if the character is a letter (a-z or A-Z)
        if char.isalpha():
            # Convert the character to lowercase
            char_lower = char.lower()
            # Loop through each character in the remaining part of the string after index i
            for j in range(i + 1, len(string)):
                # Get the character at index j
                other_char = string[j]
                # Check if the character is a letter (a-z or A-Z)
                if other_char.isalpha():
                    # Convert the character to lowercase
                    other_char_lower = other_char.lower()
                    # If the characters at index i and index j are not the same, add a palindrome of length 5 consisting of the two characters in the opposite order to the set of palindromes
                    if char_lower != other_char_lower:
                        palindrome = "{}{}".format(other_char_lower, char_lower)
                        # Check if the palindrome has a length of at least 5
                        if len(palindrome) >= 5:
                            # Add the palindrome to the set of palindromes
                            palindromes.add(palindrome)
    return palindromes
