
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of English letters in the given string between indices 3 and 7, both inclusive
    for i in range(3, 8):
        for j in range(i+1, 8):
            # Check if the substring formed by the letters between indices i and j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # If it is a palindrome, add it to the set of palindromes
                palindromes.add(string[i:j])
    
    # Return the set of palindromes
    return palindromes
