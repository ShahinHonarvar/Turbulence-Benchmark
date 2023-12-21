 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(8, 10):
        # Check if the current character is a letter (not a space or punctuation)
        if string[i].isalpha():
            # Add the current character to the palindrome being built
            palindrome = string[i]
            # Loop through each character in the string from the next character to the end of the string
            for j in range(i + 1, len(string)):
                # Check if the current character is a letter (not a space or punctuation)
                if string[j].isalpha():
                    # Add the current character to the palindrome being built
                    palindrome += string[j]
            # If the length of the palindrome is at least 3, add it to the set of palindromes
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
