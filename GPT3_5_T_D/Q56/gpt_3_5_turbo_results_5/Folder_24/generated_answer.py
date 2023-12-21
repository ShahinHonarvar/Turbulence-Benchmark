
def all_substring_of_size_n(string):
    substr_list = []
    n = len(string)
    for i in range(n-51):
        substrs = []
        for j in range(i, i+52):
            substrs.append(string[j])
        if len(set(substrs)) == 52:
            substr_list.append(''.join(substrs))
    return substr_list
