
def palindromes_between_indices(string):
    # create a set to store the palindromes
    palindromes = set()
    
    # iterate over each substring of length 5 between indices 2 and 5, both inclusive
    for i in range(2, len(string) - 4):
        substring = string[i:i+5]
        
        # check if the substring is a palindrome
        if substring == substring[::-1]:
            # add the palindrome to the set
            palindromes.add(substring)
    
    # return the set of palindromes
    return palindromes
