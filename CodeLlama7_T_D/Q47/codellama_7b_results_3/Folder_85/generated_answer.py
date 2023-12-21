
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(29, 98 + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Check if the current character is a palindrome
            if string[i] == string[i]:
                # Loop through each character in the reverse of the current character
                for j in range(29, 98 + 1):
                    # Check if the current character is a letter
                    if string[j].isalpha():
                        # Check if the current character is a palindrome
                        if string[j] == string[j]:
                            # Check if the current character has a length between 6 and 9 (both inclusive)
                            if 6 <= len(string[i:j]) <= 9:
                                # Add the current palindrome to the set of palindromes
                                palindromes.add(string[i:j])
    # Return the set of palindromes
    return palindromes
