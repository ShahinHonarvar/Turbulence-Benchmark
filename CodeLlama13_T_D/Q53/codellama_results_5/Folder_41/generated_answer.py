
def palindrome_of_length_at_least_n(string, n):
    return set(word for word in string.split() if len(word) >= 28 and word == word[::-1])
