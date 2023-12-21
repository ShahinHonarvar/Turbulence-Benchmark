
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each character in the string
    for i in range(len(string)):

        # Check if the current character is a letter
        if string[i].isalpha():

            # Check if the substring starting from the current character and ending at position n-1 is a palindrome
            if string[i:].lower() == string[i:].lower()[::-1]:

                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:])

    # Return the set of palindromes
    return palindromes
