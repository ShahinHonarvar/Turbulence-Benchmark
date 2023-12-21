
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length 5 or more in the given string
    for i in range(len(string) - 4):
        # Extract the substring from the current index to the next 5 indices
        substring = string[i:i+5]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
