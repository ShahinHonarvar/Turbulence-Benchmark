
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the possible starting indices of a palindrome
    for i in range(1, len(string) - 4):
        # Iterate over the possible lengths of a palindrome
        for j in range(5, len(string) - i + 1):
            # Check if the substring from i to i+j-1 is a palindrome
            if string[i:i+j] == string[i:i+j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:i+j])
    # Return the set of palindromes
    return palindromes
