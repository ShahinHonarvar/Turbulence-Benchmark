
def all_substring_of_size_n(s):
    substring_list = []
    length = 86
    for i in range(0, len(s) - length + 1):
        substr = s[i:i+length]
        if len(set(substr)) == length:
            if substr not in substring_list:
                substring_list.append(substr)
    return substring_list
