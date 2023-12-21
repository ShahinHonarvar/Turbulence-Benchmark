
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(len(string)):
        # Get the substring starting from index i to index len(string) - 1
        substring = string[i:len(string)]
        # Check if the substring is a palindrome of length at least 7
        if len(substring) >= 7 and substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
