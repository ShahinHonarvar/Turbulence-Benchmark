
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the string
    for i in range(len(string)):

        # Check if the character at position i is a palindrome of length n
        if string[i:i+n] == string[i:i+n][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+n])

    # Return the set of palindromes
    return palindromes
