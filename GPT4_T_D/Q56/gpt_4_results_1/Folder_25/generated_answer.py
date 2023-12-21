
def all_substring_of_size_n(s):
    return list(set(s[i: i + 67] for i in range(len(s)) if len(set(s[i: i + 67])) == 67))
