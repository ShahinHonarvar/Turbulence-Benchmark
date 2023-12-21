import re
def all_substring_of_size_n(s):
    if len(s) < 24:
        return []
    else:
        str_list = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                str_list.append(s[i:j+1])
        return sorted(set(str_list))
