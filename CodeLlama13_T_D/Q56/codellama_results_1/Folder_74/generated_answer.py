
def all_substring_of_size_n(s):
    n = 97
    return [''.join(i) for i in zip(*[iter(s)]*n)]
