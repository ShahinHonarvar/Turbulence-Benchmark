
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over all possible starting indices
    for i in range(len(string) - 3):
        # Check if the substring starting at index i has length 4 or more
        if len(string[i:]) < 4:
            continue

        # Check if the substring starting at index i is a palindrome
        if string[i:] == string[i:][::-1]:
            palindromes.add(string[i:])
    return palindromes
