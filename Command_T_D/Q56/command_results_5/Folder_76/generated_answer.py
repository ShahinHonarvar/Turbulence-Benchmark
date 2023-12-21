import re
def all_substring_of_size_n(s):
    str_list = re.findall(r'(.){149}', s)
    return list(set(str_list))
