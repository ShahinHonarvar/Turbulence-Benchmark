
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Loop through each character in the string

    for i in range(len(string)):

        # Check if the current character is a letter (A-Z)

        if string[i].isalpha():

            # Check if the current character is the same as the previous character

            if i > 0 and string[i] == string[i - 1]:

                # Add the palindrome to the set of palindromes

                palindromes.add(string[i])

    return palindromes
