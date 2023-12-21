 def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a space or other non-letter character)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the substring starting at index i and ending at index len(string) - 1
            for j in range(i, len(string)):
                # Check if the character is a letter (not a space or other non-letter character)
                if string[j].isalpha():
                    # Add the character to the palindrome string
                    palindrome += string[j]
            # Check if the palindrome has length equal to 57
            if len(palindrome) == 57:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
