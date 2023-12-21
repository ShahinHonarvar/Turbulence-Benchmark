
def palindrome_of_length_n(string, length=279):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the characters in the string

    for i in range(len(string)):

        # Check if the character is a letter (not a space or other character)

        if string[i].isalpha():

            # Check if the substring starting at position i and having length equal to length is a palindrome

            if string[i:i+length] == string[i:i+length][::-1]:

                # Add the palindrome to the set of palindromes

                palindromes.add(string[i:i+length])

    # Return the set of palindromes

    return palindromes
