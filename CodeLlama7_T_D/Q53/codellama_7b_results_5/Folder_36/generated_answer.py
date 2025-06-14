 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from the current character and extending to the end of the string
        substr = string[i:]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
