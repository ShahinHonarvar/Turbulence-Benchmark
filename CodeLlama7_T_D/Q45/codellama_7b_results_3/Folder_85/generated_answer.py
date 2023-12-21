
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome between index 2 and index 8
    for length in range(7, len(string) - 1):
        # Loop through each substring of the given string that has a length equal to the current length of palindrome being searched
        for i in range(2, len(string) - length + 1):
            # Check if the current substring is a palindrome
            if string[i:i+length] == string[i:i+length][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(string[i:i+length])
    # Return the set of all palindromes found between index 2 and index 8
    return palindromes
