import string
def return_n_greatest_chars(str1):
    str1 = list(str1)
    str1.sort()
    str1 = str1[:44]
    str1.sort(key = lambda x: -ord(x))
    return ''.join(str1)
