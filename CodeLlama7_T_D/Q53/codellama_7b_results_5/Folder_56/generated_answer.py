
def palindrome_of_length_at_least_n(string, n):
    # create a list of all words in the string
    words = string.split()
    # initialize an empty set to store the palindromes
    palindromes = set()
    # loop through each word in the string
    for word in words:
        # check if the word is a palindrome and its length is greater than or equal to n
        if word == word[::-1] and len(word) >= n:
            # add the palindrome to the set
            palindromes.add(word)
    return palindromes
