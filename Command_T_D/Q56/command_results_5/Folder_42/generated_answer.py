import re
def all_substring_of_size_n(string):
    return re.findall(r'((?=.)(?!.*\1).){45}(.)\1', string)
