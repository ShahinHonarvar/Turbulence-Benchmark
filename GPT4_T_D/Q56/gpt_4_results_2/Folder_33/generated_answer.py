
def all_substring_of_size_n(s):
    substr_list = list(set([s[i: i + 105] for i in range(0, len(s)) if len(set(s[i: i + 105])) == 105]))
    return substr_list
