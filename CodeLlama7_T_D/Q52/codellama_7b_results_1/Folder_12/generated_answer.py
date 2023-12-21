
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive matching
    lowercase_string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the string
    for i in range(len(lowercase_string)):

        # Check if the current character is a letter (a-z)
        if lowercase_string[i].isalpha():

            # Extract the substring starting from the current character to the end of the string
            substr = lowercase_string[i:]

            # Check if the substring is a palindrome
            if substr == substr[::-1]:

                # Add the palindrome to the set
                palindromes.add(substr)

    return palindromes
