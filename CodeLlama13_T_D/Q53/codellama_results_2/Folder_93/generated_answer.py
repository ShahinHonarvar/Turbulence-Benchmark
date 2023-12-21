
def palindrome_of_length_at_least_n(string):
    return {word for word in string.lower().split() if len(word) >= 90 and word == word[::-1]}
