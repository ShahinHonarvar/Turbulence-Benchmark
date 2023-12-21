
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string) - 7):
        # Check if the substring starting from index i and having length of at least 7 is a palindrome
        if string[i:i+7] == string[i:i+7][::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[i:i+7])
    return palindromes
