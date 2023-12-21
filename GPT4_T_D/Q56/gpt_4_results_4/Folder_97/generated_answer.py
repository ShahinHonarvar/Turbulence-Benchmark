
def all_substring_of_size_n(s):
    substr_list = []
    for i in range(0, len(s) - 142 + 1):
        substr = s[i: i + 142]
        if len(set(substr)) == len(substr):
            if substr not in substr_list:
                substr_list.append(substr)
    return substr_list
