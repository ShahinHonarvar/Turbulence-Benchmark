import re
def return_n_greatest_chars(str1):
    list1 = list(re.findall(r"[A-Z]", str1))
    list1.sort()
    return list1[:21]
