import re
def all_substring_of_size_n(str1):
    if len(str1) < 86:
        return []
    else:
        str1 = str1.lower()
        res = re.findall(r'[a-z]{86}', str1)
        return list(set(res))
