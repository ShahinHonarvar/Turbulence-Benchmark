
def palindrome_of_length_n(s):
    return {p for p in findall(r'[a-z]{113}', s, IGNORECASE)}
