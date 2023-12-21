
def palindrome_of_length_at_least_n(string, n):
    return set([word for word in string.lower().split() if len(word) >= n and word == word[::-1]])
