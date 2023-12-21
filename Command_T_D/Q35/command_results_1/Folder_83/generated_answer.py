import re
def remove_repeat_chars(s):
    return re.sub(r'(\w){100}(?!\1){200}(\w)', r'\1', s)
