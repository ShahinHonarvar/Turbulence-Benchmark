
def palindrome_of_length_n(string):
    # Check if the input string is empty
    if not string:
        return set()

    # Create a set to store all palindromes of length n
    palindromes = set()

    # Iterate over the characters in the input string
    for i in range(len(string)):
        # Get the substring starting at index i and ending at index len(string) - 1
        substr = string[i:len(string)]

        # Check if the substring is a palindrome
        if is_palindrome(substr):
            # Add the palindrome to the set
            palindromes.add(substr)

    # Return the set of all palindromes of length n found in the input string
    return palindromes
