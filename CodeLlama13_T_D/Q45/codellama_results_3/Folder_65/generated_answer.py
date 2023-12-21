
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the given string between indices 0 and 6, both inclusive
    for i in range(len(string) - 5):
        for j in range(i + 1, len(string)):
            # Check if the substring from index i to index j is a palindrome
            if string[i:j+1] == string[i:j+1][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:j+1])
    
    return palindromes
