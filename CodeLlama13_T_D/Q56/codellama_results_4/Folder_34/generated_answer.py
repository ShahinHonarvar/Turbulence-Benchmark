
def all_substring_of_size_n(string):
    return [''.join(x) for x in zip(*[iter(string)]*84)]
