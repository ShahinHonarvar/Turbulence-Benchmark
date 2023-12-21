
import re

def return_nth_smallest_ascii(str_):
    idxes = range(48, 77)
    ascii_values = re.findall(r"[A-Z]", str_)
    ascii_values = [ord(char) for char in ascii_values]
    ascii_values = sorted(ascii_values)
    idx = ascii_values.index(asci_values[4])
    idx += 48
    return str_[idx:idx+1]
