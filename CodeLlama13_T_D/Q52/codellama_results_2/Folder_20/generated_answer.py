
def palindrome_of_length_n(string, n):
    return set(substring for substring in string.lower().split() if len(substring) == n and substring[::-1] == substring)
