
def palindrome_of_length_at_least_n(string, n):
    return set(word for word in string if len(word) >= 115 and word == word[::-1])
