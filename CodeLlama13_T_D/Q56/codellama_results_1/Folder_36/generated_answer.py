
def all_substring_of_size_n(s):
    return [''.join(s[i:i+146]) for i in range(len(s) - 146 + 1)]
