
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible starting index
    for i in range(2, 9):
        # Loop through each possible ending index
        for j in range(i + 1, 9):
            # Check if the substring between indices i and j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    # Return the set of palindromes
    return palindromes
