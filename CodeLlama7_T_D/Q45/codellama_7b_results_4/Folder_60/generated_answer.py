
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, len(string) + 1):
        # Check if the substring starting at index i and ending at index i is a palindrome
        if string[i:] == string[i:][::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i:])
    # Return the set of palindromes
    return palindromes
