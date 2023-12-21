
def palindromes_of_specific_lengths(string, length_range, index_range):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the characters in the specified index range

    for i in range(index_range[0], index_range[1] + 1):

        # Check if the current character is a letter (uppercase or lowercase)

        if string[i].isalpha():

            # Iterate over the characters in the substring from the current index to the end of the string

            for j in range(i, len(string)):

                # Check if the substring from the current index to the end of the string is a palindrome

                if string[i:j + 1] == string[i:j + 1][::-1]:

                    # Add the palindrome to the set of palindromes

                    palindromes.add(string[i:j + 1])

    # Return the set of palindromes that meet the requirements specified in the function arguments

    return palindromes
