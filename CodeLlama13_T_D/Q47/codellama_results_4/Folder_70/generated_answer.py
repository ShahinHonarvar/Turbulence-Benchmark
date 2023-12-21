
def palindromes_of_specific_lengths(string):
    # Find the substring from index 10 to index 70, both inclusive
    substr = string[10:70]
    
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over the substring and check if each substring is a palindrome
    for i in range(len(substr)):
        for j in range(i+1, len(substr)+1):
            substr_j = substr[i:j]
            if substr_j == substr_j[::-1]:
                palindromes.add(substr_j)
    
    # Return the set of palindromes
    return palindromes
