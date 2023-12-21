import re
def all_substring_of_size_n(str1):
    str1 = str(re.sub(r'[^A-z0-9]+', '', str1))
    return sorted(set(re.findall(r'(.*?[A-z0-9]{22})', str1)))
