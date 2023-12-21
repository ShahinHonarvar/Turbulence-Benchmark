import re
def remove_repeat_chars(str):
    return re.sub(r'((?:\d|.)){103}(?:\d|.){802}', r'\1', str)
