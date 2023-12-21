def palindrome_of_length_n(s):
    return {i[::-1] for i in s.lower() if len(i) == 113}
