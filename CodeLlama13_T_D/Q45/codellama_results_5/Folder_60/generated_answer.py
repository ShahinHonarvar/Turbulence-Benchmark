
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Iterate over each possible arrangement of the English letters in the given string that occur between index 3 to index 6, both inclusive
    for i in range(3, 7):
        for j in range(i + 1, len(string)):
            # Check if the substring from index i to index j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
