
def palindrome_of_length_at_least_n(s, n):
    return {word for word in s if len(word) >= n and word == word[::-1]}
