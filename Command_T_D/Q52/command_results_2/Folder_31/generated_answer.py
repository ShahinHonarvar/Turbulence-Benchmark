def palindrome_of_length_n(s):
    return {
        p
        for p in set(s.lower())
        if len(p) == 66 and p[0] == p[-1] and p[1:-1] == p[2:-2]
    }
