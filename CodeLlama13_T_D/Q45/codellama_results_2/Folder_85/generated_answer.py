
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each possible arrangement of English letters in the given string
    for i in range(2, 8 + 1):
        for j in range(i, len(string) - i + 1):
            # Check if the substring between indices i and j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
