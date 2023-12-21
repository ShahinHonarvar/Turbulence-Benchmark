 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 4 in the given string
    for i in range(len(string) - 3 + 1):
        # Extract the substring starting from index i and with length at least 4
        substring = string[i:i+4]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the substring to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
