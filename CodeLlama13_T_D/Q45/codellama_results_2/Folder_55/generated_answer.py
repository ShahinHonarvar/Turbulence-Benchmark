
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each possible arrangement of English letters in the given string
    for i in range(len(string) - 2):
        for j in range(i + 1, len(string)):
            # Check if the substring between indices i and j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
