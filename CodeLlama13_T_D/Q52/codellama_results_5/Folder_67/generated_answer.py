
def palindrome_of_length_n(s):
    return {substr for substr in set(s) if len(substr) == 42 and substr == substr[::-1]}
