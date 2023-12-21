
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Loop through each character in the string

    for i in range(len(string)):

        # Check if the substring starting from index i and has length n is a palindrome

        if string[i:i+n] == string[i:i+n][::-1]:

            # Add the palindrome to the set of palindromes

            palindromes.add(string[i:i+n])

    # Return the set of palindromes

    return palindromes
