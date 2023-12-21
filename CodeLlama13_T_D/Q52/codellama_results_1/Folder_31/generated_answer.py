
def palindrome_of_length_n(string):
    return {substring for substring in string.lower().split() if len(substring) == 66 and substring[::-1] == substring}
