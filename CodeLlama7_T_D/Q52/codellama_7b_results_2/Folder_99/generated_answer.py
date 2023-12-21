
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate through each character in the string
    for i in range(len(string)):
        # Get the substring starting at index 'i' and ending at index 'i + n - 1', where 'n' is the length of the palindrome
        substr = string[i:i + n - 1]

        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)

    # Return the set of all palindromes found in the string
    return palindromes
