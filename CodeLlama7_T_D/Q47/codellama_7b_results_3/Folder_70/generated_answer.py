 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(10, 71):
        # Check if the character at index i is a letter (not punctuation or digit)
        if string[i].isalpha():
            # Check if the character at index i + 1 is a letter (not punctuation or digit)
            if string[i + 1].isalpha():
                # Check if the two characters at index i and i + 1 form a palindrome
                if string[i] == string[i + 1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:i + 2])
    # Return the set of palindromes found in the specified index range
    return palindromes
