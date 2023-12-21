 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 6
    for i in range(len(string) - 5):
        # Extract the substring and convert it to lowercase
        substr = string[i:i+6].lower()
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
