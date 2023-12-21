
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 3 in the given string that occurs between indices 7 and 9, both inclusive
    for i in range(7, 10):
        for j in range(i+2, len(string)):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    # Return the set of all palindromes found in the given string
    return palindromes
