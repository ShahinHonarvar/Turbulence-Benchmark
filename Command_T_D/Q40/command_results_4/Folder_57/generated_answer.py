import re
def return_n_smallest_chars(str):
    str_dict = {}
    for m in re.finditer(r'[A-z]', str):
        str_dict[m.group()] = m.start()
    return [str[i] for i in sorted(str_dict.keys(), key=lambda x: str_dict[x])][:29]
