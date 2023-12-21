
def palindrome_of_length_n(string):
    return set(substring for substring in string if substring[::-1] == substring)
