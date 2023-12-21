
def palindrome_of_length_n(string, n):
    # Check if the input string is valid
    if not isinstance(string, str) or len(string) == 0:
        return set()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate through each substring of length n in the input string
    for i in range(len(string) - n + 1):

        # Check if the current substring is a palindrome
        if string[i:i+n] == string[i:i+n][::-1]:

            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:i+n])

    # Return the set of palindromes
    return palindromes
