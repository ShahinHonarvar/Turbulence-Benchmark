
def palindrome_of_length_at_least_n(s, n):
    return set([word for word in s.split() if len(word) >= 137 and word == word[::-1]])
