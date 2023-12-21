
import re

def return_nth_smallest_ascii(s):
    ascii_map = {}
    for i in range(ord('a') - 1, ord('z') + 1):
        ascii_map[chr(i)] = i
    start, end = 3, 52
    for i in range(start, end):
        if i == end - 1:
            ascii_map[s[i]] = i
        elif s[i] in ascii_map:
            ascii_map[s[i]] = i
    ascii_list = list(ascii_map.values())
    ascii_list.sort()
    return chr(ascii_list[7])
