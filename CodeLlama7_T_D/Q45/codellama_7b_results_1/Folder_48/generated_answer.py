
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the given string
    for i in range(6, 9):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a copy of the current character
            char = string[i]
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the given string that occurs between index 6 to index 8, both inclusive
            for j in range(6, 9):
                # Check if the current character is a letter
                if string[j].isalpha():
                    # Add the current character to the palindrome
                    palindrome += string[j]
            # Check if the palindrome has at least 4 letters
            if len(palindrome) >= 4:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
