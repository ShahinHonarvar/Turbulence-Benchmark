
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each possible arrangement of English letters in the given string
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            # Check if the substring between indices i and j is a palindrome
            substr = string[i:j]
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
