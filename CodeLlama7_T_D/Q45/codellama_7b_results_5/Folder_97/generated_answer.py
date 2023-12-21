
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible arrangement of the English letters in the given string that occur between index 0 to index 4, both inclusive
    for i in range(5):
        # Loop through each possible arrangement of the English letters in the given string that occur between index 0 to index 4, both inclusive
        for j in range(i + 1, 6):
            # Check if the substring starting from index i and ending at index j is a palindrome
            if string[i:j].lower() == string[i:j][::-1].lower():
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:j])
    return palindromes
