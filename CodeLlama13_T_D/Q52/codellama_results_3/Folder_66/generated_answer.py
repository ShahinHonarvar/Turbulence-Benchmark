
def palindrome_of_length_n(string):
    string = string.lower()  # convert the input string to lowercase
    palindromes = set()  # initialize an empty set to store the palindromes
    for i in range(len(string) - 24):  # iterate over each substring of length 25
        substr = string[i:i+25]  # extract the current substring
        if substr == substr[::-1]:  # check if the substring is a palindrome
            palindromes.add(substr)  # add the palindrome to the set
    return palindromes  # return the set of all palindromes found
