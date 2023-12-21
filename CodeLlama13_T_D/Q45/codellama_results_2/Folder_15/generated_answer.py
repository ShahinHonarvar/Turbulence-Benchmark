
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each possible arrangement of English letters in the given string
    for i in range(1, len(string)):
        for j in range(i + 2, len(string) + 1):
            # Extract the substring between indices i and j
            substr = string[i:j]

            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)

    return palindromes
