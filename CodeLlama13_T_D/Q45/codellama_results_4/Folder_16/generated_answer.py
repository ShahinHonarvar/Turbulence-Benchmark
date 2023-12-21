
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each possible substring of length 5 between indices 6 and 9 (inclusive)
    for i in range(6, 10):
        for j in range(i+4, 10):
            # Extract the substring and check if it is a palindrome
            substr = string[i:j]
            if substr == substr[::-1]:
                # If it is a palindrome, add it to the set of palindromes
                palindromes.add(substr)

    return palindromes
