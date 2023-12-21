import re
def all_substring_of_size_n(s):
    return re.findall(r"(\A[a-z]){30}([a-z]\Z)", s)
