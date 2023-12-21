def palindrome_of_length_at_least_n(text):
    return set(w for w in text.lower() if len(w) >= 47 and w[::-1] == w)
