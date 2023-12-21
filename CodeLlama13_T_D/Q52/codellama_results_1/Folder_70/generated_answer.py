
def palindrome_of_length_n(s):
    return set(word for word in s.split() if len(word) == 401 and word == word[::-1])
