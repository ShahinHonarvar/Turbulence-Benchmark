import re
def return_n_greatest_chars(s):
    m = re.findall(r'([A-Z])', s)
    return sorted(m, key=lambda x: ord(x), reverse=True)[:32]
