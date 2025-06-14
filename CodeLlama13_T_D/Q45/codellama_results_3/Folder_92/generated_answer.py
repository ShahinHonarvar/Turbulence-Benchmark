
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Loop through each substring of length 4 to 7 in the given string
    for i in range(4, 8):
        for j in range(len(string) - i + 1):
            # Check if the substring is a palindrome
            if string[j:j+i] == string[j+i-1::-1]:
                # Add the palindrome to the set
                palindromes.add(string[j:j+i])

    # Return the set of palindromes
    return palindromes
