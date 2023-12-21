
def palindromes_between_indices(string):
    # Create a list of all possible palindromes of length 6 or more
    palindromes = []
    for i in range(1, len(string) - 5):
        # Check if the substring starting at index i has a palindrome form
        substr = string[i:]
        if substr == substr[::-1]:
            # If it does, add it to the list of palindromes
            palindromes.append(substr)
    return set(palindromes)
