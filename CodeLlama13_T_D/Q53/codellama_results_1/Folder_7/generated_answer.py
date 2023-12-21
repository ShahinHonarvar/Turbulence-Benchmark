
def palindrome_of_length_at_least_n(s):
    return {word for word in s.split() if len(word) >= 12 and word == word[::-1]}
