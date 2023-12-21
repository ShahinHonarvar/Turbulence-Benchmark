import sys
def return_n_greatest_chars(s):
    char_list = []
    for c in s:
        if ord(c) > ord(max(char_list, key=lambda x: ord(x))):
            char_list.append(c)
    return char_list[:29]
