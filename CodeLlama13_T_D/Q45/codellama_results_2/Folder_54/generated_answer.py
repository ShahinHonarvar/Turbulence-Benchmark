
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the given string that occur between indices 4 and 9, both inclusive
    for i in range(4, len(string) - 3):
        for j in range(i + 1, len(string) - 2):
            # Check if the substring formed by the English letters between indices i and j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:j])
    
    return palindromes
