
def palindrome_of_length_n(string):
    # Remove any non-letter characters from the string
    string = ''.join([c for c in string if c.isalpha()])
    # Convert the string to lowercase
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the length of the string
    for i in range(len(string)):
        # Check if the substring is a palindrome
        if string[i:].lower() == string[i:].lower()[::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:])
    # Return the set of all palindromes
    return palindromes
