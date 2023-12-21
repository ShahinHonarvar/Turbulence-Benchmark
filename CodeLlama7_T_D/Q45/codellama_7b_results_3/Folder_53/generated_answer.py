
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, 8 + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the uppercase version of the current character
            upper_char = string[i].upper()
            # Loop through each character in the string from index 4 to index 8 (inclusive)
            for j in range(4, 8 + 1):
                # Check if the current character is the same as the previous character
                if upper_char == string[j].upper():
                    # If the current character is the same as the previous character, check if it is a letter or not
                    if string[j].isalpha():
                        # If the current character is a letter, add it to the palindrome
                        palindrome = string[:i] + string[i] + string[i + 1:]
                        # Check if the palindrome has at least 6 characters and add it to the set of palindromes
                        if len(palindrome) >= 6:
                            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
