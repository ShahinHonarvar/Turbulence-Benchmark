
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible subsequence of the given string that occurs between index 6 and index 8, both inclusive
    for i in range(6, 9):
        # Get the substring of the given string that occurs between index 6 and index i, both inclusive
        substr = string[6:i+1]
        # Check if the substring is a palindrome of length at least 4
        if substr == substr[::-1] and len(substr) >= 4:
            # Add the palindrome to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes in a case-insensitive manner
    return {x.lower() for x in palindromes}
