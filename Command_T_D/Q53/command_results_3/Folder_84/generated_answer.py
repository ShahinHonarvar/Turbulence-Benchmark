def palindrome_of_length_at_least_n(s):
    return {a for a in s.lower() if len(a) >= 81 and a == a[::-1].lower()}
