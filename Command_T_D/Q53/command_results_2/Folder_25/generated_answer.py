def palindrome_of_length_at_least_n(s):
    if not s:
        return set()
    if len(s) <= 1:
        return set()
    return set(s[i:j] for i in range(0, len(s) - 1) for j in range(i + 1, len(s)))
