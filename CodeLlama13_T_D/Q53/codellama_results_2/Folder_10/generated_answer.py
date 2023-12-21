
def palindrome_of_length_at_least_n(string):
    return set(word for word in string.lower().split() if len(word) >= 92 and word == word[::-1])
