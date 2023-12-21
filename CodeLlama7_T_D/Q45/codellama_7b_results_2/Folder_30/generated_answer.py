 def palindromes_between_indices(string):
    # Set of all possible palindromes of length at least 4
    palindromes = set()
    # Loop through each substring of the given string
    for i in range(len(string) - 3):
        # Check if the substring is a palindrome
        if string[i:i + 4] == string[i:i + 4][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i + 4])
    return palindromes
