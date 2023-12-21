
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each possible arrangement of the English letters in the given string
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            # Check if the current substring is a palindrome and has length at least 3
            if string[i:j] == string[i:j][::-1] and len(string[i:j]) >= 3:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    return palindromes
