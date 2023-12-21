import re
def return_n_smallest_chars(str):
    str = re.sub(r'[^A-Z]', '', str)
    if len(str) == 0:
        return []
    else:
        return sorted(list(str), key=lambda x: ord(x) - ord('A'))
