
def palindrome_of_length_at_least_n(string, n):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the characters in the string

    for i in range(len(string)):

        # Check if the character is a letter (not a space or a digit)

        if string[i].isalpha():

            # Check if the substring starting from the current character and ending at the end of the string is a palindrome

            if string[i:] == string[i:][::-1]:

                # Add the palindrome to the set

                palindromes.add(string[i:])

    # Return the set of all palindromes of length greater than or equal to 54 that exist in the given string

    return palindromes
