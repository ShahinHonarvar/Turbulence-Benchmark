def palindrome_of_length_n(s):
    return {a for a in set(s.lower()) if a == a[::-1] and len(a) == 77}
