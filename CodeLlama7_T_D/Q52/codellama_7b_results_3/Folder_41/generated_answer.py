
def palindrome_of_length_n(string):
    # Convert the string to lowercase
    string = string.lower()
    # Create an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting at index i and having length equal to n
        substr = string[i:i+n]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
