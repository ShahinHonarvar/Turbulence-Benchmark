
def palindrome_of_length_n(string):
    return set([word for word in string.split() if len(word) == 100 and word == word[::-1]])
