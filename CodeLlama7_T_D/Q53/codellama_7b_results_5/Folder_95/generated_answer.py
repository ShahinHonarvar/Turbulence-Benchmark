
def palindrome_of_length_at_least_n(string, n=35):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is not an English letter, continue to the next iteration
        if not char.isalpha():
            continue

        # Create a substring of length n starting from index i
        substr = string[i:i+n]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
