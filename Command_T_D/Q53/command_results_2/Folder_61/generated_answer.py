def palindrome_of_length_at_least_n(text):
    if len(text) < 5:
        return set()
    return set(x for x in text.lower() if x == x[::-1])
