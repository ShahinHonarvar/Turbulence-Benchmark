
def palindrome_of_length_at_least_n(s, n):
    # create a set to store the palindromes
    palindromes = set()
    # loop through each substring of length greater than or equal to 20 in the input string
    for i in range(len(s) - n + 1):
        # check if the substring is a palindrome
        if s[i:i+n] == s[i:i+n][::-1]:
            # add the palindrome to the set of palindromes
            palindromes.add(s[i:i+n])
    return palindromes
