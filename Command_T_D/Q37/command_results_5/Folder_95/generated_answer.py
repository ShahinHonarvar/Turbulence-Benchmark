import re
def filter_chars(s):
    return re.sub(r"([\w]+)\W{35}(\w)+\W{40}\W{35}(\w)+\W{40}(.)+", r"\1 \3 \4", s)
