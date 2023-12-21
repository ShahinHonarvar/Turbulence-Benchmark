
def palindrome_of_length_at_least_n(s, n):
    # Check if the input string is valid
    if not s or len(s) < 2:
        return []

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the input string
    for i in range(len(s)):

        # Check if the current character is a letter
        if s[i].isalpha():

            # Check if the substring starting at the current character and ending at the end of the input string is a palindrome
            if s[i:] == s[i:][::-1]:

                # Add the palindrome to the set
                palindromes.add(s[i:])

    # Return the set of palindromes
    return palindromes
