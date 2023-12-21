
def palindrome_of_length_n(s):
    n = 69
    return set([word for word in s.lower().split() if len(word) == n and word[::-1] == word])
