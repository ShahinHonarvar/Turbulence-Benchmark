
def palindromes_between_indices(string):
    # Create a list of all possible palindromes of length at least 6
    palindromes = []
    for i in range(5, len(string) - 5):
        # Check if the substring starting from index i and ending at index i + 11 is a palindrome
        if string[i:i+11] == string[i:i+11][::-1]:
            # If it is a palindrome, add it to the list of palindromes
            palindromes.append(string[i:i+11])
    return set(palindromes)
