import re
def return_n_smallest_chars(str1):
    #find all unique characters
    str1 = re.findall(r"[A-Za-z]", str1)
    #sort them by ascii value
    str1.sort(key=lambda x: ord(x))
    #take the first 47
    return str1[:47]
