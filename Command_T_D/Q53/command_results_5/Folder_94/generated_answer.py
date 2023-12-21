def palindrome_of_length_at_least_n(text):
    letters = set(text.lower())
    return {w for w in text.split() if len(w) >= 41 and w == w[::-1] and all(c in letters for c in w)}
