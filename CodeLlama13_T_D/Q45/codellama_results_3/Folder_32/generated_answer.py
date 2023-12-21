
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 5 in the string
    for i in range(1, len(string) - 4):
        # Check if the substring is a palindrome
        if string[i:i+5] == string[i:i+5][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+5])
    
    return palindromes
