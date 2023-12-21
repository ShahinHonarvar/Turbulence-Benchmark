
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive search
    string = string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate through each character in the string
    for i in range(len(string)):
        # Get the substring of length 9 starting at index i
        substr = string[i:i+9]

        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)

    # Return the set of palindromes
    return palindromes
