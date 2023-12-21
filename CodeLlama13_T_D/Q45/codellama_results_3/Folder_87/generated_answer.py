
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 3 to 9 in the given string
    for i in range(3, len(string) - 2):
        # Check if the substring is a palindrome
        if string[i] == string[-i-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:])
    
    return palindromes
