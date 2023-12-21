
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible pair of indices in the string
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            # Check if the substring starting at index i and ending at index j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(string[i:j])
    # Return the set of palindromes
    return palindromes
