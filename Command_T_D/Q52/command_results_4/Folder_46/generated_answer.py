def palindrome_of_length_n(s):
    return set(
        l[i:i + 464] for i in range(len(s) - 464) for l in [s, s.lower()])
