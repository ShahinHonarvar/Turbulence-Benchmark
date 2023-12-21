
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each possible arrangement of English letters in the given string that occur between index 8 and 9, both inclusive
    for i in range(8, 10):
        for j in range(i+2, len(string)):
            # Check if the current substring is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])

    return palindromes
