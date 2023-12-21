
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 3 in the given string
    for i in range(4, len(string) - 2):
        # Get the substring of length at least 3 starting from index i
        substring = string[i:i+3]
        # Check if the substring is a palindrome in a case-insensitive manner
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of all palindromes found
    return palindromes
