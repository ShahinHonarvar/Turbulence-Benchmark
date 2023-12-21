import re
def return_n_greatest_chars(s):
    ascii_dict = {char:i for i,char in enumerate(sorted(set(re.findall(r'[a-z0-9]', s)))}
    return [char for char in s if ascii_dict[char] in range(1, 50)]
