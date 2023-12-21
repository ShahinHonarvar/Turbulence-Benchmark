
def palindromes_between_indices(string, start_index, end_index):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the indices in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Create a palindrome by mirroring the string around index i
            palindrome = string[:i] + string[i:][::-1]
            # Add the palindrome to the set of palindromes
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
