import re
def filter_chars(s):
    return re.sub(r'[a-zA-Z][\d]{2}|[A-Z][\d]{2}|[a-zA-Z][\d]{3}|[A-Z][\d]{3}|[a-zA-Z][\d]{4}|[A-Z][\d]{4}|[a-zA-Z][\d]{5}|[A-Z][\d]{5}|[a-zA-Z][\d]{6}|[A-Z][\d]{6}', '', s)
