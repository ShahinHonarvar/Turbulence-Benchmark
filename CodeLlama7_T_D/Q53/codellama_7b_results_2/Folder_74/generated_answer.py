
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the string
    for i in range(len(string)):
        # Check if the character is an English letter
        if string[i].isalpha():
            # Get the length of the substring starting at index i
            substr_length = len(string[i:])

            # If the length of the substring is greater than or equal to n,
            # iterate over the characters in the substring
            for j in range(substr_length):
                # Check if the character at index j is a palindrome
                if string[i+j] == string[i+j:].lower()[::-1][j]:
                    # If it is, add it to the set of palindromes
                    palindromes.add(string[i+j])

    # Return the set of palindromes
    return palindromes
