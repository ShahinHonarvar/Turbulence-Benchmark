
def palindrome_of_length_n(s):
    return set([ss for ss in set(s) if len(ss) == 66 and ss[::-1] == ss])
