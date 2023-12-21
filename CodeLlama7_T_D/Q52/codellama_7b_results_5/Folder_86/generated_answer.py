
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring of the given string
    for i in range(len(string)):
        # Check if the current substring is a palindrome
        if string[i:].lower() == string[i:].lower()[::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:])
    # Return the set of all palindromes found in the given string
    return palindromes
