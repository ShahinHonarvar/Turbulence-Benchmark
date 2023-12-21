
def palindrome_of_length_n(string, n):
    # Check if the input string is a palindrome of length n
    if len(string) < n:
        return []

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the input string
    for i in range(len(string)):

        # Check if the substring starting at position i has length n
        if len(string[i:]) == n:

            # Add the palindrome to the set
            palindromes.add(string[i:i+n])

    # Return the set of palindromes
    return palindromes
