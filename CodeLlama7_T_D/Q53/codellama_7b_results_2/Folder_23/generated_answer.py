
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each substring of length greater than or equal to n in the given string
    for i in range(len(string) - n + 1):

        # Check if the substring is a palindrome in a case-insensitive manner
        if string[i:i+n].lower() == string[i:i+n].lower()[::-1]:

            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:i+n])

    # Return the set of all palindromes of length greater than or equal to 19 that exist in the given string
    return palindromes
