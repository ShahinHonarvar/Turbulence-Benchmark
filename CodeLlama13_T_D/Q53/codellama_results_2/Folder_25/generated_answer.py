
def palindrome_of_length_at_least_n(string):
    return {word for word in string.split() if len(word) >= 38 and word == word[::-1]}
