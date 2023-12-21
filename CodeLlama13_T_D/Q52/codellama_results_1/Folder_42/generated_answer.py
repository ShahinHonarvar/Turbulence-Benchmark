
def palindrome_of_length_n(s):
    return {substring for substring in s if substring == substring[::-1]}
