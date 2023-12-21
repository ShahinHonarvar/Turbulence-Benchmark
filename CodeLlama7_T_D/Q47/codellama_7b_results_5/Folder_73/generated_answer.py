
def palindromes_of_specific_lengths(string, length_range=(22, 33), index_range=(21, 62)):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over each character in the substring of interest

    for i in range(index_range[0], index_range[1] + 1):

        # Check if the current character is a letter (i.e., not a space or punctuation)

        if string[i].isalpha():

            # Initialize an empty string to store the palindrome

            palindrome = ""

            # Iterate over each character in the substring of interest, starting from the current character and moving backwards

            for j in range(i, index_range[0] - 1, -1):

                # Append each character to the palindrome string

                palindrome += string[j]

            # Check if the palindrome has the required length and is a valid English word

            if len(palindrome) in range(length_range[0], length_range[1] + 1) and palindrome.isalpha():

                # Add the palindrome to the set of palindromes

                palindromes.add(palindrome)

    # Return the set of palindromes

    return palindromes
