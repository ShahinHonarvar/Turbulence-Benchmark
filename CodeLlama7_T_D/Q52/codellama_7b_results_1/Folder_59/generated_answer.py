 def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the character to uppercase
            uppercase_letter = string[i].upper()
            # Loop through each character in the string starting from the current index
            for j in range(i + 1, len(string) + 1):
                # Check if the substring starting from the current index is a palindrome
                if uppercase_letter == string[j - 1].upper():
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:j])
    # Return the set of palindromes
    return palindromes
