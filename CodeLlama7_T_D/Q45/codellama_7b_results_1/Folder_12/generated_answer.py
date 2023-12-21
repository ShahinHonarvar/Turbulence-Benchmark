
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the possible substrings of length 4 or more
    for i in range(len(string) - 3):
        # Get the substring starting at index i and ending at index i + 3
        substring = string[i:i + 4]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
