
def palindrome_of_length_n(string):
    # Check if the input string is empty or None
    if not string:
        return set()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each character in the input string
    for i in range(len(string)):

        # Check if the current character is a letter
        if string[i].isalpha():

            # Create a substring of length n starting at index i
            substr = string[i:i+n]

            # Check if the substring is a palindrome
            if substr == substr[::-1]:

                # Add the palindrome to the set
                palindromes.add(substr)

    # Return the set of all palindromes of length n as substrings of the input string
    return palindromes
