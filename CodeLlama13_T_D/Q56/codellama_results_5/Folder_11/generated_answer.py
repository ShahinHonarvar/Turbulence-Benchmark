
def all_substring_of_size_n(s):
    return ["".join(x) for x in zip(*[iter(s)]*78)]
