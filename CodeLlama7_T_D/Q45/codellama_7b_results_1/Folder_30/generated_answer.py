
def palindromes_between_indices(string, start=0, end=None):
    # Check if the string is empty
    if not string:
        return set()

    # Set the default value for the end index
    if end is None:
        end = len(string) - 1

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the possible starting indices
    for i in range(start, end + 1):

        # Check if the substring starting at index i is a palindrome
        if string[i:] == string[i:][::-1]:

            # Add the palindrome to the set
            palindromes.add(string[i:])

    return palindromes
