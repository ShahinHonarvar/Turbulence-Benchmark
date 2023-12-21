
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
            # Loop through each character in the string starting from index i + 1
            for j in range(i + 1, len(string)):
                # Get the character at index j
                other_char = string[j]
                # If the character is a letter (uppercase or lowercase) and it is not the same as the first character
                if other_char.isalpha() and char_lower != other_char.lower():
                    # Check if the two characters are the same when converted to uppercase
                    if char_lower == other_char.upper():
                        # If the two characters are the same when converted to uppercase, add the palindrome to the set of palindromes
                        palindromes.add(string[i:j+1])
                    # Check if the two characters are the same when converted to lowercase
                    elif char_lower == other_char.lower():
                        # If the two characters are the same when converted to lowercase, add the palindrome to the set of palindromes
                        palindromes.add(string[i:j+1])
    # Return the set of palindromes
    return palindromes
