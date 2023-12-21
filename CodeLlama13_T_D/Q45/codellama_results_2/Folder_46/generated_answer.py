
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over each possible arrangement of the English letters in the given string that occur between index 4 to index 9, both inclusive
    for i in range(4, 10):
        for j in range(i + 1, 10):
            # Create a palindrome from the current indices and add it to the set if it is of length at least 6
            palindrome = string[i:j]
            if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    # Return the set of all palindromes
    return palindromes
