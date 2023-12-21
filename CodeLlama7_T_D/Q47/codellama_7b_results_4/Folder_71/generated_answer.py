 def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    lengths = range(23, 37)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the substrings of the specified length in the given string
    for i in range(18, 65):
        substring = string[i:i+lengths]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
