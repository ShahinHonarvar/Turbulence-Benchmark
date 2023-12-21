
def palindromes_of_specific_lengths(string):
    # Initialize the set of palindromes
    palindromes = set()
    # Loop through each substring between indices 200 and 300
    for i in range(200, 301):
        # Check if the substring is a palindrome
        if string[i:i+1] == string[i:i+1][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:i+1])
    # Return the set of palindromes
    return palindromes
