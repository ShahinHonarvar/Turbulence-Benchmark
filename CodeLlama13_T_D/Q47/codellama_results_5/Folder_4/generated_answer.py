
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring from index 12 to index 92, both inclusive
    substr = string[12:93]
    palindromes = []
    for i in range(len(substr)):
        # Check if the substring from index i to index len(substr) is a palindrome
        if substr[i:] == substr[i:][::-1]:
            # Add the palindrome to the list of palindromes
            palindromes.append(substr[i:])
    return set(palindromes)
