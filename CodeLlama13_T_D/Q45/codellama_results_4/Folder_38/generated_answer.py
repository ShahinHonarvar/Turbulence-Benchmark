
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate through each possible arrangement of the English letters in the given string that occur between index 3 to index 8, both inclusive
    for i in range(3, 9):
        for j in range(i+1, len(string)):
            # Check if the substring from indices i to j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j])
    
    return palindromes
