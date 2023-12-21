
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate through each substring of length n in the given string
    for i in range(len(string) - 100 + 1):
        # Check if the current substring is a palindrome
        if string[i:i+100] == string[i:i+100][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+100])

    # Return the set of all palindromes of length equal to 100
    return palindromes
