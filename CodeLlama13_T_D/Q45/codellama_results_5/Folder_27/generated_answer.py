
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each possible arrangement of the English letters in the given string that occur between index 2 to index 8, both inclusive
    for i in range(2, 9):
        for j in range(i + 1, 9):
            # Check if the substring formed by the English letters between indices i and j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
