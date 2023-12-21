
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(2, len(string) - 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Create a copy of the string without the letter at index i
            no_letter_string = string[:i] + string[i+1:]
            # Iterate over the characters in the no_letter_string
            for j in range(2, len(no_letter_string) - 1):
                # Check if the character at index j is a letter
                if no_letter_string[j].isalpha():
                    # Create a copy of the no_letter_string without the letters at indices i and j
                    no_letters_string = no_letter_string[:i] + no_letter_string[i+1:] + no_letter_string[j+1:]
                    # Check if the length of the no_letters_string is greater than or equal to 4
                    if len(no_letters_string) >= 4:
                        # Create a palindrome from the letters in the no_letters_string
                        palindrome = no_letters_string[::-1]
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
