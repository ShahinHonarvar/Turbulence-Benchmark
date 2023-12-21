
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of the English letters in the given string that occur between index 1 to index 5, both inclusive
    for i in range(1, 6):
        for j in range(i, len(string) - (5 - i)):
            # Check if the substring from index i to index j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    return palindromes
