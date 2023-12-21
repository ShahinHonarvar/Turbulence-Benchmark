
import re

def return_nth_smallest_ascii(str_input):
    str_input = re.sub(r'[^A-Z0-9]+', '', str_input)
    ASCII_VALUES = list(str_input)
    return ASCII_VALUES[len(ASCII_VALUES)-9]
