
def all_substring_of_size_n(s):
    substr_list = list(set([s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(s[i:j]) == 46 and len(set(s[i:j])) == 46]))
    return substr_list
