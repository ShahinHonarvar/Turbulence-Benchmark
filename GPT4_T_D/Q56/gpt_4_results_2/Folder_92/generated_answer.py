
def all_substring_of_size_n(s):
    length = len(s)
    substr_list = []
    for i in range(length - 8):
        substr = s[i:i+9]
        if len(substr) == len(set(substr)):
            substr_list.append(substr)
    return list(set(substr_list))
