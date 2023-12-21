
def palindromes_of_specific_lengths(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Define a set to store the palindromes
    palindromes = set()

    # Iterate over the substring from index 18 to index 98, both inclusive
    for i in range(18, 98 + 1):

        # Check if the character at position i is a letter (a-z) or not
        if string[i].isalpha():

            # Define a variable to store the palindrome
            palindrome = ""

            # Iterate over the substring from index i - 18 to index i, both inclusive
            for j in range(i - 18, i + 1):

                # Check if the character at position j is a letter (a-z) or not
                if string[j].isalpha():

                    # Add the character at position j to the palindrome
                    palindrome += string[j]

            # Check if the palindrome has the required length
            if len(palindrome) >= 31 and len(palindrome) <= 51:

                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
