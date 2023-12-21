
def all_substring_of_size_n(s):
    substr_list = []
    for i in range(len(s)-95):
        substr = s[i:i+96]
        if len(set(substr)) == len(substr):
            if substr not in substr_list:
                substr_list.append(substr)
    return substr_list
