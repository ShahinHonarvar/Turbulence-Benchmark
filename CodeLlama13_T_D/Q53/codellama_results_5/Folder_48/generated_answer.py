
def palindrome_of_length_at_least_n(string):
    return set(word for word in string.split() if len(word) >= 150 and word == word[::-1])
