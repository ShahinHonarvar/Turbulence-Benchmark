
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Loop through each possible arrangement of English letters in the given string
    for i in range(7, 10):
        for j in range(i + 2, len(string)):
            # Check if the substring from index i to index j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
