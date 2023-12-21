
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(7, 9):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a copy of the string without the current character
            temp_string = string[:i] + string[i+1:]
            # Loop through each character in the temporary string
            for j in range(len(temp_string)):
                # Check if the current character is a letter
                if temp_string[j].isalpha():
                    # Create a palindrome by reversing the characters in the temporary string
                    palindrome = ''.join(reversed(temp_string[j:]))
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
