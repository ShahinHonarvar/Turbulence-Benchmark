
def palindromes_between_indices(s):
    # Create a list of all possible palindromes of length at least 3
    palindromes = []
    for i in range(len(s) - 2):
        # Create a substring that starts at index i and ends at index i + 2
        substr = s[i:i+3]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the list
            palindromes.append(substr)
    return set(palindromes)
