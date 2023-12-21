
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
            # Check if the substring starting at the current character and ending at the end of the input string is a palindrome
            if string[i:].lower() == string[i:].lower()[::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:])

    # Return the set of palindromes of length 47 where each palindrome is a substring of the given string
    return palindromes
