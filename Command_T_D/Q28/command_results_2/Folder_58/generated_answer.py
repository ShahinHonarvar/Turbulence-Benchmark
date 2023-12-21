
import re

def return_nth_smallest_ascii(s):
    ascii_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_int = ord('A')
    index = len(s) // 2
    if index >= 26:
        return ascii_str[index - 26]
    else:
        ascii_str_list = [char for char in s if char in ascii_str]
        ascii_int_list = [ord(char) for char in ascii_str_list]
        ascii_int_list.sort()
        return ascii_str[ascii_int_list[index] - ascii_int]
