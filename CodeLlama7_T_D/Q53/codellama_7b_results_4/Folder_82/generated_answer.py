
def palindrome_of_length_at_least_n(string, n):
    # create a dictionary to store the palindromes
    palindromes = {}

    # loop through each character in the string
    for i in range(len(string)):
        # check if the current character is a letter
        if string[i].isalpha():
            # check if the current character is the same as the previous character
            if string[i] == string[i-1]:
                # add the palindrome to the dictionary
                palindromes[(string[i], string[i-1])] = True
    # return the set of all palindromes of the length greater than or equal to 72 that exist in the given string
    return set(palindromes.keys())
