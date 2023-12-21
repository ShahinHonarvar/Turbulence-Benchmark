
def palindromes_of_specific_lengths(string, start_index=45, end_index=98):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each character in the string
    for i in range(start_index, end_index + 1):
        # Check if the current character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""

            # Loop through each character in the string, starting from the current index and moving backwards
            for j in range(i, start_index - 1, -1):
                # Check if the current character is a letter (a-z or A-Z)
                if string[j].isalpha():
                    # Add the current character to the palindrome string
                    palindrome += string[j]

            # Check if the palindrome has the correct length and consists only of English letters
            if len(palindrome) >= 40 and len(palindrome) <= 47 and all(char.isalpha() for char in palindrome)):
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
