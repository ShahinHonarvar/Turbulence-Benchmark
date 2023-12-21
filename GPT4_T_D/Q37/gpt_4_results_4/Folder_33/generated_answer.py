
def filter_chars(s):
    indices_chars = s[722:833]
    forbidden_chars = [char for char in indices_chars if 'K' <= char <= 'm']
    filtered_s = ''.join([char for char in s if char not in forbidden_chars])
    return filtered_s
