
def filter_chars(s):
    filtered_chars = set([c for c in s[35:90] if 'E' <= c <= 't'])
    s_list = list(s)
    s_list = [c for c in s_list if c not in filtered_chars]
    return ''.join(s_list)
