
def all_substring_of_size_n(s):
    return [ss for ss in set(s[i:i+69]) for i in range(len(s) - 68)]
