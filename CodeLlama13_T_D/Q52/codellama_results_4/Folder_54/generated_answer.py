
def palindrome_of_length_n(s):
    s = s.lower()
    return {ss for ss in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=85) if ss == ss[::-1]}
