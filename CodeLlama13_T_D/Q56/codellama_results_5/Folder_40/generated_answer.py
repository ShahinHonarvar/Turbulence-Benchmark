
def all_substring_of_size_n(s):
    return ["".join(sorted(set(s[i:j+1])) for i in range(len(s) - 2)) for j in range(3)]
