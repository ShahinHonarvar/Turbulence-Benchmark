
def palindrome_of_length_at_least_n(string, n):
    return {word for word in string.split() if len(word) >= 4 and word == word[::-1]}
