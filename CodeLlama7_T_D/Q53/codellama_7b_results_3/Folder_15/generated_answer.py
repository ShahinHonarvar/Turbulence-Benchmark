
def palindrome_of_length_at_least_n(string, n=4):
    # Convert the string to lowercase for case-insensitive search
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the characters in the string

    for i in range(len(string)):

        # Check if the character is a letter

        if string[i].isalpha():

            # Check if the substring starting from the current character and ending at the end of the string is a palindrome

            if string[i:] == string[i:][::-1]:

                # Add the palindrome to the set

                palindromes.add(string[i:])

    return palindromes
