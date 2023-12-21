import re
def filter_chars(s):
    return re.sub(r'[^-v]{%221; 419}'.format(s), '', s)
