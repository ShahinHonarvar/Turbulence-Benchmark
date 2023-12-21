
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(75, 96):
        # Check if the substring starting at index i and having a length of 9 is a palindrome
        if string[i:i+9] == string[i:i+9][::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i:i+9])
    # Return the set of palindromes
    return palindromes
