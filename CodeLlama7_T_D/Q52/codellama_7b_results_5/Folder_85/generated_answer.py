
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the string
    for i in range(len(string)):
        # Check if the character at position i is a palindrome of length 46
        if string[i:i+46] == string[i:i+46][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+46])

    # Return the set of palindromes found in the given string
    return palindromes
