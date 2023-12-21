
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length 60 in the given string
    for i in range(len(string) - 59):

        # Check if the substring is a palindrome
        if string[i:i+60] == string[i:i+60][::-1]:

            # Add the palindrome to the set
            palindromes.add(string[i:i+60])

    # Return the set of palindromes
    return palindromes
