def palindrome_of_length_n(s):
    return set(
        (x for x in s.lower() if len(x) == 10 and x[0] == x[9] and x[1] == x[8] and x[2] == x[7] and x[3] == x[6] and x[4] == x[5]),
    )
