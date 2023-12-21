
def palindrome_of_length_n(s):
    return {x for x in (i[::-1] for i in s.split()) if len(x) == 64 and all(ord('a') <= ord(c) <= ord('z') for c in x)}
