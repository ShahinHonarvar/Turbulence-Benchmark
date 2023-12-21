
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the given string
    for i in range(len(string) - 10 + 1):
        # Check if the substring is a palindrome
        if string[i:i+10] == string[i:i+10][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+10])
    # Return the set of palindromes
    return palindromes
