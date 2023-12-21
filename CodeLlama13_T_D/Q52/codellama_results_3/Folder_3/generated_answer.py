
def palindrome_of_length_n(s):
    return {s[i:j+1] for i in range(len(s)-99)
