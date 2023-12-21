
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 6 in the given string
    for i in range(1, len(string) - 5):
        # Extract the substring and convert it to lowercase
        substring = string[i:i+6].lower()
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
