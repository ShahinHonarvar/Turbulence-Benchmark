
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over each substring of length n in the given string

    for i in range(len(string) - 26 + 1):

        # Check if the substring is a palindrome

        if string[i:i+27] == string[i:i+27][::-1]:

            # Add the palindrome to the set

            palindromes.add(string[i:i+27])

    # Return the set of all palindromes of length 27 as substrings of the given string

    return palindromes
