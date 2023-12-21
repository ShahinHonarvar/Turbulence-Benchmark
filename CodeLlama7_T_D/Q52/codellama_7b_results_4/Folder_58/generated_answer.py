
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from the current character and having length equal to the specified length
        substr = string[i:i+223]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
