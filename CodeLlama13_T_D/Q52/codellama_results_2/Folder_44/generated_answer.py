
def palindrome_of_length_n(string, n):
    return set([word for word in string.split() if len(word) == n and word.lower() == word[::-1]])
