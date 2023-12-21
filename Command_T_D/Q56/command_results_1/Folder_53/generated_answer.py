import re
def all_substring_of_size_n(s):
    if not s:
        return []
    return [x for x in re.findall(r'(?<=.)\w{25}', s)]
