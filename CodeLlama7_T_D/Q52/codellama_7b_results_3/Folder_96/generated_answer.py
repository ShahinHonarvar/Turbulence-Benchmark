
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Loop through each character in the string

    for i in range(len(string)):

        # Check if the character is a letter (not a space or any other character)

        if string[i].isalpha():

            # Check if the substring starting at index i and having length n is a palindrome

            if string[i:i+n] == string[i:i+n][::-1]:

                # Add the palindrome to the set

                palindromes.add(string[i:i+n])

    # Return the set of all palindromes of length n in the given string

    return palindromes
