
def all_substring_of_size_n(s):
    return [''.join(s[i:i+31]) for i in range(len(s)-30)]
