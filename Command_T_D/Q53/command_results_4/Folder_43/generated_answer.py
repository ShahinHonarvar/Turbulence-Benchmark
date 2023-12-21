def palindrome_of_length_at_least_n(text):
    return set(text.lower().split()) & {k for k in range(len(text), 1, -1) if k % 2 == 0 and k > 49}
