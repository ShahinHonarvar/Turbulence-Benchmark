
def palindromes_of_specific_lengths(string, indices=(45, 98)):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the indices in the specified range
    for i in range(*indices):
        # Check if the character at the current index is a letter
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""

            # Iterate over the characters in the substring starting from the current index
            for j in range(i, *indices):
                # Add the character to the palindrome string
                palindrome += string[j]

                # Check if the palindrome string has a length between 40 and 47 (both inclusive)
                if len(palindrome) >= 40 and len(palindrome) <= 47:
                    # Convert the palindrome string to lowercase for case-insensitive comparison
                    palindrome = palindrome.lower()

                    # Check if the palindrome string is a palindrome
                    if palindrome == palindrome[::-1]:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)

            # Break out of the loop if any palindromes have been found
            if len(palindromes) > 0:
                break

    # Return the set of palindromes
    return palindromes
