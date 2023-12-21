 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length 6 or more in the given string
    for i in range(len(string) - 5):
        # Check if the substring is a palindrome
        if string[i:i+6] == string[i:i+6][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+6])
    return palindromes
