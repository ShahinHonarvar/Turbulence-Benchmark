
def palindrome_of_length_n(s):
    return set(word for word in s if word == word[::-1])
