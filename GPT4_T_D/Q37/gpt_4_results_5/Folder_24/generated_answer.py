
def filter_chars(s):
    s_list = list(s)
    chars_to_remove = set([_ for _ in s_list[36:80] if '2' <= _ <= 's'])
    return ''.join([_ for _ in s_list if _ not in chars_to_remove])
