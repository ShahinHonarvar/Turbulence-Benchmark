import re
def return_n_greatest_chars(str1):
    list_of_chars = []
    for c in str1:
        if ord(c) not in list(range(ord('a'), ord('z') + 1)):
            list_of_chars.append(c)
    list_of_chars.sort()
    list_of_chars = list_of_chars[:19]
    return list_of_chars
