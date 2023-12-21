def palindrome_of_length_n(s):
    if len(s) < 78:
        return set()
    return set(s[i:j] for i in range(len(s) - 1) for j in range(i, len(s)))
