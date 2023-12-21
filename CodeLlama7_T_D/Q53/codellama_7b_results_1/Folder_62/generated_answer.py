
def palindrome_of_length_at_least_n(string, n):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Create a set to store all the palindromes of length greater than or equal to 31
    palindromes = set()

    # Loop through each character in the string
    for i in range(len(string)):

        # Check if the current character is a letter (uppercase or lowercase)
        if string[i].isalpha():

            # Create a substring of length 31 starting from the current character and ending at the last character of the string
            substr = string[i:min(len(string), i + 31)]

            # Check if the substring is a palindrome (same when read forward or backward)
            if substr == substr[::-1]:

                # Add the palindrome to the set of palindromes
                palindromes.add(substr)

    # Return the set of palindromes found in the given string
    return palindromes
