
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each possible arrangement of English letters in the given string between indices 3 and 8, both inclusive
    for i in range(3, 9):
        for j in range(i + 4, len(string)):
            # Extract the substring from index i to index j and check if it is a palindrome
            substr = string[i:j]
            if substr == substr[::-1]:
                # If it is a palindrome, add it to the set of palindromes
                palindromes.add(substr)

    return palindromes
