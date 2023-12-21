
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 6 in the given string
    for i in range(4, len(string) - 8 + 1):
        # Extract the substring from the given string that occurs between index 4 to index 8, both inclusive
        substring = string[i:i+8]
        # Check if the substring is a palindrome in a case-insensitive manner
        if substring == substring[::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
