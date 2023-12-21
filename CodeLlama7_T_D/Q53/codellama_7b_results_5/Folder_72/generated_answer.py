
def palindrome_of_length_at_least_n(string, n):
    # initialize an empty set to store the palindromes
    palindromes = set()
    # loop through each word in the string
    for word in string.split():
        # check if the word is a palindrome with length greater than or equal to n
        if word == word[::-1] and len(word) >= n:
            # add the palindrome to the set
            palindromes.add(word)
    # return the set of palindromes
    return palindromes
