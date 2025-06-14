
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each index in the specified range
    for i in range(3, 10):
        # Get the substring starting from the current index
        substring = string[i:]
        # Loop through each character in the substring
        for j in range(len(substring)):
            # Get the palindrome by reversing the substring
            palindrome = substring[j:][::-1]
            # Add the palindrome to the set if it is of length at least 3 and it does not contain any non-letter characters
            if len(palindrome) >= 3 and all(c.isalpha() for c in palindrome):
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
