
def all_substring_of_size_n(s):
    return [''.join(c) for c in itertools.product(*zip(s, s[1:])) if len(set(c)) == 143]
