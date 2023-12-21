
def palindrome_of_length_n(s, n):
    return {substr for substr in s.split() if len(substr) == n and substr == substr[::-1]}
