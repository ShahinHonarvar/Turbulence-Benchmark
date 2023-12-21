
def palindrome_of_length_at_least_n(string, n=11):
    # create a set to store the palindromes
    palindromes = set()
    # loop through each substring of length greater than or equal to n in the input string
    for i in range(len(string) - n + 1):
        # check if the substring is a palindrome
        if string[i:i+n] == string[i:i+n][::-1]:
            # add the palindrome to the set
            palindromes.add(string[i:i+n])
    return palindromes
