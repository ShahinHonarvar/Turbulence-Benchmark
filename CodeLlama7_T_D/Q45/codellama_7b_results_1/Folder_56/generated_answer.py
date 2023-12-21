
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each index in the range specified
    for i in range(5, 10):
        # Create a substring of the given string starting from index i and ending at index i + 2
        substring = string[i:i + 2]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substring)
    return palindromes
