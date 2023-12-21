import re
def remove_repeat_chars(s):
    return re.sub(r'((?=([^aieou]))\1)+', '', s[90:-200])
