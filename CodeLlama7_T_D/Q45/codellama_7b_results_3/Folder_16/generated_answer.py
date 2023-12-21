
def palindromes_between_indices(string, start_index, end_index):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length at least 5 in the given string
    for i in range(start_index, end_index + 1 - 4):
        # Get the substring of length at least 5
        substring = string[i:i+5]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    return palindromes
