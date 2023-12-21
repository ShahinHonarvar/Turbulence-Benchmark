
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the string
    for i in range(len(string)):

        # Check if the current character is a letter
        if string[i].isalpha():

            # Check if the current character is the same as the previous character
            if i > 0 and string[i] == string[i - 1]:

                # If the current character is the same as the previous character, then we have found a palindrome of length 2
                palindromes.add(string[i:i + 2])

    # Return the set of all palindromes of length equal to 40, where each palindrome is a substring of the given string
    return palindromes
