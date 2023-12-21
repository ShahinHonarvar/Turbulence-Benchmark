
def palindrome_of_length_n(string, n):
    return {substring for substring in string.lower().split() if len(substring) == n and substring == substring[::-1]}
