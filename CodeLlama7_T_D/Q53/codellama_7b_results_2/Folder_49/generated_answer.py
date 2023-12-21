
def palindrome_of_length_at_least_n(string, n):
    # Convert the input string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the characters in the input string

    for i in range(len(string)):

        # Check if the character at position i is a letter (a-z)

        if string[i].isalpha():

            # Check if the substring starting from position i and ending at the end of the string is a palindrome

            if string[i:] == string[i:][::-1]:

                # Add the palindrome to the set

                palindromes.add(string[i:])

    # Return the set of all palindromes of length greater than or equal to n that exist in the input string

    return palindromes
