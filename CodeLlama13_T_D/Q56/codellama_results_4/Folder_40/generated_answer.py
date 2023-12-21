
def all_substring_of_size_n(s):
    return ["".join(i) for i in zip(*[iter(s)]*2) if ''.join(i).count('a') < 2]
