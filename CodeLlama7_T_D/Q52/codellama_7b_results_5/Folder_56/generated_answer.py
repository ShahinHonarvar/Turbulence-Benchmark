
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the given string
    for i in range(len(string) - 95 + 1):
        # Extract the substring of length n starting at position i in the string
        substring = string[i:i+95]
        # Check if the substring is a palindrome in a case-insensitive manner
        if substring == substring[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
