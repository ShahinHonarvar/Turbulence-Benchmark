import re
def all_substring_of_size_n(s):
    return re.findall(r'(.*?){22}(.*?)'.format(22), s)
