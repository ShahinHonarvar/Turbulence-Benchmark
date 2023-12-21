
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each substring of length at least 5 in the given string
    for i in range(len(string) - 4):
        # Extract the substring starting from index i and ending at index (i + 4)
        substring = string[i:i + 5]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes formed from the English letters in the given string that occur between index 4 to index 7, both inclusive
    return palindromes
