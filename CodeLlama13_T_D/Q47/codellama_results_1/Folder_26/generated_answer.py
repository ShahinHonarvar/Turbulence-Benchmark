
def palindromes_of_specific_lengths(string):
    # find the substring from index 24 to index 84, both inclusive
    substr = string[24:85]
    
    # create a set to store the palindromes
    palindromes = set()
    
    # loop through each length between 21 to 31 (both inclusive)
    for length in range(21, 32):
        # loop through each index in the substring
        for i in range(len(substr)):
            # check if the current index is a palindrome of the specified length
            if substr[i:i+length] == substr[i+length-1::-1]:
                # add the palindrome to the set
                palindromes.add(substr[i:i+length])
    
    return palindromes
