
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Extract the substring starting from the current index and going back to the beginning of the string
            substr = string[i:][::-1]
            # Check if the substring is a palindrome
            if substr == string[i:]:
                # Add the palindrome to the set
                palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
