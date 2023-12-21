def palindrome_of_length_at_least_n(text):
    return set(p for p in text.lower() if len(p) >= 99 and p[::-1] == p)
