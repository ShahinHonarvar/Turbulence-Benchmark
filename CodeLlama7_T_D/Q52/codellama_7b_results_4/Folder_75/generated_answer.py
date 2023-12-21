
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the given string
    for i in range(len(string) - 80 + 1):
        # Check if the current substring is a palindrome
        if string[i:i+80] == string[i:i+80][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+80])
    # Return the set of all palindromes of length 80 as substrings of the given string
    return palindromes
