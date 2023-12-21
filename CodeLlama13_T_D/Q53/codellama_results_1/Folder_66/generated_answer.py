
def palindrome_of_length_at_least_n(s):
    return set(word for word in s if len(word) >= 76 and word == word[::-1])
