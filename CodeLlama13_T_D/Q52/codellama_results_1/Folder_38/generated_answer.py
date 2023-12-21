
def palindrome_of_length_n(s):
    return set([ss for ss in [''.join(sorted(''.join(p))) for p in zip(*[iter(s)]*38) if len(set(p)) == 1] if ss == ss[::-1]])
