
def palindromes_between_indices(string):
    # initialize an empty set to store the palindromes
    palindromes = set()
    # loop through each character in the string
    for i in range(1, len(string) - 7 + 1):
        # extract a substring of length 7 from the current position in the string
        substr = string[i:i+7]
        # check if the substring is a palindrome
        if substr == substr[::-1]:
            # add the palindrome to the set
            palindromes.add(substr)
    # return the set of palindromes
    return palindromes
