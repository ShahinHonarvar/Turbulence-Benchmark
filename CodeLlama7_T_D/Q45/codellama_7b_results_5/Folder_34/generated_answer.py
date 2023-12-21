
def palindromes_between_indices(string, start, end):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for length in range(start, end + 1):
        # Create a substring of the given string that is of the current length
        substring = string[start:end + 1]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of all palindromes found in the given string between the specified indices
    return palindromes
