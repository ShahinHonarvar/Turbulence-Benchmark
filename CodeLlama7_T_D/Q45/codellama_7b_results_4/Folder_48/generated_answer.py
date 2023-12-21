
def palindromes_between_indices(s):
    # Check if the given string is a palindrome
    if s == s[::-1]:
        return {s}

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the given string
    for i in range(len(s)):

        # Check if the character at index i is a letter
        if s[i].isalpha():

            # Create a substring of the given string that starts at index i and ends at index 8 (inclusive)
            substr = s[i:8]

            # Check if the substring is a palindrome
            if substr == substr[::-1]:

                # Add the palindrome to the set of palindromes
                palindromes.add(substr)

    # Return the set of palindromes
    return palindromes
