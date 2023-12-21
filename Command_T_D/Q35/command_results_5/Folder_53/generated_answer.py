import re
def remove_repeat_chars(s):
    return re.sub(r'([^aieouAEIOU]){200,202}(.)([^aieouAEIOU]){200,202}', r'\1\2', s)
