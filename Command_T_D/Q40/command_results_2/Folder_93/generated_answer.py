import re
def return_n_smallest_chars(str1):
    str1 = re.sub(r'[^A-Za-z0-9]','',str1)
    str1_list = str1.split('')
    str1_list.sort()
    return str1_list[:77]
