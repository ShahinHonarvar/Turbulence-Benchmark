
def palindromes_between_indices(string):
    # Create a list of all possible palindromes of length 3 or more
    palindromes = []
    for i in range(len(string) - 2):
        # Check if the substring starting at index i and ending at index i + 2 is a palindrome
        substr = string[i:i + 2]
        if substr == substr[::-1]:
            # Add the palindrome to the list
            palindromes.append(substr)
    return set(palindromes)
