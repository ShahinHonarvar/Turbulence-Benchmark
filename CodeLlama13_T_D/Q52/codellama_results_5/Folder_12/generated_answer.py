
def palindrome_of_length_n(s):
    return set(word for word in s.lower().split() if len(word) == 23 and word[::-1] == word)
