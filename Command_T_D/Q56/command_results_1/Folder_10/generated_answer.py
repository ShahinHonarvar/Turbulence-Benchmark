import re
def all_substring_of_size_n(str1):
    return re.findall(r'(?<=.)(.)\1{55}', str1)
