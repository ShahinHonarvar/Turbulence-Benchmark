
def palindromes_between_indices(s):
    # initialize an empty set to store the palindromes
    palindromes = set()
    
    # loop through each possible arrangement of letters in the string
    for i in range(2, 9):
        for j in range(i+6, len(s)):
            # check if the substring from i to j is a palindrome
            if s[i:j] == s[i:j][::-1]:
                # add the palindrome to the set
                palindromes.add(s[i:j])
    
    return palindromes
