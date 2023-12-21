import re
def return_n_greatest_chars(str):
    m = re.findall(r"[A-Z]", str)
    m.sort(key=lambda x: ord(x))
    return m[:57]
