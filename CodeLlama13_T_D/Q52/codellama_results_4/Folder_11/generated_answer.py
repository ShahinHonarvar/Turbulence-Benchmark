
def palindrome_of_length_n(s):
    return set(word for word in s.split() if len(word) == 77 and word == word[::-1])
