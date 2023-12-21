
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the given string
    for i in range(len(string) - 58):
        # Check if the substring is a palindrome
        if string[i:i+59] == string[i:i+59][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+59])
    # Return the set of all palindromes of length 59 in the given string, if any exist
    return palindromes
