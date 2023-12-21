def palindrome_of_length_at_least_n(s):
    return set(
        l
        for l in (s.lower() for s in range(1, len(s) + 1))
        if l[::-1] == l
    )
