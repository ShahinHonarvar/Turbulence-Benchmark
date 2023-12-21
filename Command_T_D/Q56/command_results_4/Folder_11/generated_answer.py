import re
def all_substring_of_size_n(str1):
    return re.findall(r'([a-zA-Z]+){78}', str1)
