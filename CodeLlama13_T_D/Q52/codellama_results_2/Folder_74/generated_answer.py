
def palindrome_of_length_n(string):
    return set(substring for substring in string if len(substring) == 96 and substring.lower() == substring[::-1].lower())
