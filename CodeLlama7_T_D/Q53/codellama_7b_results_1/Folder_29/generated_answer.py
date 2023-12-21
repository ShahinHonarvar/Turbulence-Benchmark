
def palindrome_of_length_at_least_n(string, n):
    # create a set to store the palindromes
    palindromes = set()
    # loop through each character in the string
    for i in range(len(string)):
        # check if the current character is at least n characters from the end of the string
        if len(string) - i >= n:
            # create a substring starting at the current index and ending at the nth character from the end of the string
            substr = string[i:(len(string) - (n - 1)))]
            # check if the substring is a palindrome
            if substr == substr[::-1]:
                # add the palindrome to the set
                palindromes.add(substr)
    # return the set of palindromes
    return palindromes
