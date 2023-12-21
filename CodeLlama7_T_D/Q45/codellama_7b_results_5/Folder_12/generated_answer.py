
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, len(string) + 1):
        # Check if the substring starting at index 3 and having length i is a palindrome
        if string[i - 3:i] == string[i - 3:i][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i - 3:i])
    # Return the set of palindromes
    return palindromes
