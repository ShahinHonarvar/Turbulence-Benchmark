
def palindrome_of_length_n(string):
    # Define the set of all palindromes
    palindromes = set()
    # Loop through each substring of the given string
    for i in range(len(string) - 185):
        # Check if the substring is a palindrome
        substr = string[i:i+186]
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    return palindromes
