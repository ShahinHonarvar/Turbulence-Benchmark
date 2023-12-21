
def palindrome_of_length_n(string):
    return set(word for word in string.split() if len(word) == 99 and word[::-1] == word)
