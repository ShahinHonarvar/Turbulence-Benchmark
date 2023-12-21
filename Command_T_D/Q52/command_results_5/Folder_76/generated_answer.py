def palindrome_of_length_n(s):
    return {x for x in s.lower() if len(x) == 257 and x[0] == x[-1] and x[0] == x[int(len(x) / 2) - 1] and x[-1] == x[int(len(x) / 2)]]}
