
def palindrome_of_length_at_least_n(string, n):
    # create a set to store the palindromes
    palindromes = set()
    # loop through each character in the string
    for i in range(len(string)):
        # get the substring starting from the current index and ending at the end of the string
        substr = string[i:]
        # check if the substring is a palindrome
        if substr == substr[::-1]:
            # add the palindrome to the set
            palindromes.add(substr)
    # return the set of palindromes with length greater than or equal to n
    return {x for x in palindromes if len(x) >= n}
