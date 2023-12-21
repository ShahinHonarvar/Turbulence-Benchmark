
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(1, len(string) - 5):
        # Check if the substring starting at index i and having length 7 is a palindrome
        if string[i:i+7] == string[i:i+7][::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i:i+7])
    # Return the set of palindromes
    return palindromes
